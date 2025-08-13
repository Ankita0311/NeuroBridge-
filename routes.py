from flask import render_template, request, redirect, url_for, flash
from app import app, db
from models import EmailSignup
import re
import logging

def is_valid_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

@app.route('/')
def index():
    """Main landing page"""
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def email_signup():
    """Handle email signup form submission"""
    try:
        email = request.form.get('email', '').strip().lower()
        name = request.form.get('name', '').strip()
        user_type = request.form.get('user_type', '').strip()
        
        # Validation
        if not email:
            flash('Email address is required.', 'error')
            return redirect(url_for('index') + '#signup')
        
        if not is_valid_email(email):
            flash('Please enter a valid email address.', 'error')
            return redirect(url_for('index') + '#signup')
        
        # Check if email already exists
        existing_signup = EmailSignup.query.filter_by(email=email).first()
        if existing_signup:
            flash('This email is already registered for early access!', 'info')
            return redirect(url_for('index') + '#signup')
        
        # Create new signup
        new_signup = EmailSignup()
        new_signup.email = email
        new_signup.name = name if name else None
        new_signup.user_type = user_type if user_type else None
        
        db.session.add(new_signup)
        db.session.commit()
        
        logging.info(f"New email signup: {email}")
        flash('Thank you! You\'ve been added to our early access list.', 'success')
        
    except Exception as e:
        logging.error(f"Error in email signup: {str(e)}")
        db.session.rollback()
        flash('Sorry, there was an error processing your request. Please try again.', 'error')
    
    return redirect(url_for('index') + '#signup')

@app.route('/demo')
def demo():
    """Placeholder route for demo - could redirect to external prototype"""
    flash('Demo coming soon! Sign up for early access to be notified.', 'info')
    return redirect(url_for('index') + '#signup')
