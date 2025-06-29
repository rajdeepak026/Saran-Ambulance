from backend.models import db, Admin, Booking, Query, Fare, Partner, BlogPost
from app import app

# Create all tables
with app.app_context():
    db.create_all()
    print("✅ Tables created successfully!")

    # Insert dummy data only if tables are empty
    if not Admin.query.first():
        # Admin dummy data
        admin1 = Admin(email="admin@example.com", phone="1234567890", address="123 Admin St.")
        db.session.add(admin1)

        # Booking dummy data
        booking1 = Booking(
            pickup="Location A",
            drop="Location B",
            service="ICU Ambulance",
            name="John Doe",
            contact="9876543210"
        )
        db.session.add(booking1)

        # Query dummy data
        query1 = Query(
            name="Jane Doe",
            contact="9988776655",
            email="jane@example.com",
            message="Need help with booking"
        )
        db.session.add(query1)

        # Fare dummy data
        fare1 = Fare(
            pickup_location="Location A",
            drop_location="Location B",
            fare_amount=500.0
        )
        db.session.add(fare1)

        # Partner dummy data
        partner1 = Partner(
            name="Good Health NGO",
            logo_url="https://example.com/logo.png",
            description="Provides emergency ambulance support"
        )
        db.session.add(partner1)

        # BlogPost dummy data
        blog1 = BlogPost(
            title="How to Act in a Medical Emergency",
            slug="medical-emergency-tips",
            author="Admin",
            banner_image_url="https://example.com/banner.png",
            content="<p>Here are some important tips...</p>"
        )
        db.session.add(blog1)

        db.session.commit()
        print("✅ Dummy data inserted successfully!")
    else:
        print("ℹ️ Tables already have data. No dummy data inserted.")
