from functools import wraps
from flask import session, redirect, url_for, flash, request
from werkzeug.security import check_password_hash, generate_password_hash
from .models import User, db

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access the admin area.', 'error')
            return redirect(url_for('admin.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access the admin area.', 'error')
            return redirect(url_for('admin.login'))
        
        user = User.query.get(session['user_id'])
        if not user or not user.is_admin:
            flash('Admin access required.', 'error')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

def create_admin_user(username, email, password):
    """Create an admin user"""
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return False, "Username already exists"
    
    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        return False, "Email already exists"
    
    user = User(
        username=username,
        email=email,
        password_hash=generate_password_hash(password),
        is_admin=True
    )
    
    try:
        db.session.add(user)
        db.session.commit()
        return True, "Admin user created successfully"
    except Exception as e:
        db.session.rollback()
        return False, f"Error creating user: {str(e)}"

def authenticate_user(username, password):
    """Authenticate user login"""
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        return user
    return None