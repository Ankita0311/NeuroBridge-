from app import db
from datetime import datetime

class EmailSignup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    user_type = db.Column(db.String(50), nullable=True)  # youth, veteran, indigenous, other
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<EmailSignup {self.email}>'
