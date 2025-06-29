from datetime import datetime
from backend.database import db  # Import the shared db instance
from sqlalchemy import UniqueConstraint


class Admin(db.Model):
    """
    Model for Admin user details.
    This model stores the admin's email, phone, and address.
    In a real application, this would also include password hashing.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    # In a real app, you would add a password hash and salt for security
    # password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"Admin('{self.email}', '{self.phone}')"

class Booking(db.Model):
    """
    Model for ambulance booking requests.
    Corresponds to the 'Manage Bookings' section in bookings.html.
    """
    id = db.Column(db.Integer, primary_key=True)
    pickup = db.Column(db.String(200), nullable=False)
    drop = db.Column(db.String(200), nullable=False)
    service = db.Column(db.String(100), nullable=False) # e.g., "ICU Ambulance", "Oxygen Ambulance"
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Pending') # e.g., "Pending", "Assigned", "Completed"
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Booking('{self.name}', '{self.service}', '{self.status}')"

class Query(db.Model):
    """
    Model for user queries/help requests.
    Corresponds to the 'User Queries' section in queries.html.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=True) # Email can be optional
    message = db.Column(db.Text, nullable=False)
    received_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Query('{self.name}', '{self.received_at}')"

class Fare(db.Model):
    """
    Model for managing ambulance fares between locations.
    Corresponds to the 'Fare Management' section in index.html (dashboard).
    """
    id = db.Column(db.Integer, primary_key=True)
    pickup_location = db.Column(db.String(100), nullable=False)
    drop_location = db.Column(db.String(100), nullable=False)
    fare_amount = db.Column(db.Float, nullable=False)

    # Add a unique constraint to prevent duplicate pickup-drop-fare entries
    __table_args__ = (db.UniqueConstraint('pickup_location', 'drop_location', name='_fare_location_uc'),)

    def __repr__(self):
        return f"Fare('{self.pickup_location}' to '{self.drop_location}': ₹{self.fare_amount})"

class Partner(db.Model):
    """
    Model for ambulance service partners (hospitals, clinics, NGOs).
    Corresponds to the 'Partners Section' in index.html.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    logo_url = db.Column(db.String(200), nullable=True) # URL for the partner's logo
    description = db.Column(db.Text, nullable=True) # Short description of the partner

    def __repr__(self):
        return f"Partner('{self.name}')"

class BlogPost(db.Model):
    """
    Model for blog posts on the website.
    Corresponds to the 'Blogs Section' in index.html and the emergency_tips.html content.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False) # URL-friendly version of the title
    author = db.Column(db.String(100), nullable=False)
    publish_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    banner_image_url = db.Column(db.String(200), nullable=True) # URL for the main image
    content = db.Column(db.Text, nullable=False) # Full HTML content or Markdown

    def __repr__(self):
        return f"BlogPost('{self.title}', '{self.author}')"
