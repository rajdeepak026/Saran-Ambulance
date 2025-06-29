from flask import Flask, render_template, redirect, request, session, url_for, jsonify
from flask import current_app as app
from .models import *
from datetime import datetime # Ensure datetime is imported if not already

@app.route("/")
def index():
    return render_template("user/user-dashboard.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/admin", methods=["GET", "POST"])
def admin_dashboard():
    if request.method == "POST":
        pickup = request.form.get("pickup")
        drop = request.form.get("drop")
        fare = request.form.get("fare")
        if pickup and drop and fare:
            new_fare = Fare(pickup_location=pickup, drop_location=drop, fare_amount=float(fare))
            db.session.add(new_fare)
            db.session.commit()
            return redirect(url_for("admin_dashboard"))
    fares = Fare.query.all()
    return render_template("admin/index.html", fares=fares)

@app.route("/admin/delete-fare/<int:fare_id>", methods=["POST"])
def delete_fare(fare_id):
    fare = Fare.query.get(fare_id)
    if fare:
        db.session.delete(fare)
        db.session.commit()
    return redirect(url_for("admin_dashboard"))

@app.route("/logout")
def logout():
    return render_template("/login")

@app.route("/bookings")
def bookings():
    all_bookings = Booking.query.order_by(Booking.timestamp.desc()).all()
    return render_template("admin/bookings.html", bookings=all_bookings)

@app.route("/assign-booking/<int:booking_id>", methods=["POST"])
def assign_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    booking.status = "Assigned"
    db.session.commit()
    return redirect(url_for("bookings"))

@app.route("/delete-booking/<int:booking_id>", methods=["POST"])
def delete_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    db.session.delete(booking)
    db.session.commit()
    return redirect(url_for("bookings"))

@app.route("/queries")
def queries():
    return render_template("admin/queries.html")

@app.route("/api/queries", methods=["GET"])
def api_queries():
    all_queries = Query.query.order_by(Query.received_at.desc()).all()
    data = [{
        "id": q.id,
        "name": q.name,
        "contact": q.contact,
        "email": q.email,
        "message": q.message,
        "time": q.received_at.strftime("%Y-%m-%d %I:%M %p")
    } for q in all_queries]
    return jsonify(data)

@app.route("/api/delete-query/<int:query_id>", methods=["DELETE"])
def delete_query(query_id):
    q = Query.query.get_or_404(query_id)
    db.session.delete(q)
    db.session.commit()
    return jsonify({"success": True})

@app.route("/settings")
def setting():
    return render_template("admin/settings.html")

@app.route("/blog")
def blog():
    return render_template("user/blog")

@app.route("/user-dashboard")
def user_dashboard():
    return render_template("user/user-dashboard")

# New API endpoint to get fare data for the user dashboard
@app.route("/api/fares", methods=["GET"])
def api_fares():
    all_fares = Fare.query.all()
    fares_data = [{
        "pickup": fare.pickup_location,
        "drop": fare.drop_location,
        "amount": fare.fare_amount
    } for fare in all_fares]
    return jsonify(fares_data)

# Endpoint for handling user booking submissions
@app.route("/submit-booking", methods=["POST"])
def submit_booking():
    pickup = request.form.get("pickup")
    drop = request.form.get("drop")
    service = request.form.get("service")
    name = request.form.get("fullName")
    contact = request.form.get("contact")

    if not all([pickup, drop, service, name, contact]):
        return jsonify({"success": False, "message": "All fields are required!"}), 400

    new_booking = Booking(
        pickup=pickup,
        drop=drop,
        service=service,
        name=name,
        contact=contact,
        status="Pending", # Default status
        timestamp=datetime.utcnow() # Current UTC time
    )
    db.session.add(new_booking)
    db.session.commit()
    return jsonify({"success": True, "message": "Booking successful! We will contact you shortly."})

# Endpoint for handling user queries
@app.route("/submit-query", methods=["POST"])
def submit_query():
    name = request.form.get("name")
    contact = request.form.get("contact")
    email = request.form.get("email")
    message = request.form.get("message")

    if not all([name, contact, message]):
        return jsonify({"success": False, "message": "Name, contact, and message are required!"}), 400

    new_query = Query(
        name=name,
        contact=contact,
        email=email,
        message=message,
        received_at=datetime.utcnow()
    )
    db.session.add(new_query)
    db.session.commit()
    return jsonify({"success": True, "message": "Query submitted successfully! We will get back to you soon."})