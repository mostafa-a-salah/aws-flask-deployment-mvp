import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///esbe.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
from admin.models import db
db.init_app(app)

# Import routes after app creation to avoid circular imports
from routes import *
from admin.routes import admin_bp

# Register admin blueprint
app.register_blueprint(admin_bp)

# Create database tables
with app.app_context():
    db.create_all()

# Template filters
@app.template_filter('nl2br')
def nl2br_filter(text):
    """Convert newlines to <br> tags"""
    if text:
        return text.replace('\n', '<br>')
    return text

# Context processor for site settings
@app.context_processor
def inject_site_settings():
    from admin.utils import get_all_settings
    try:
        settings = get_all_settings()
        return {'site_settings': settings}
    except:
        return {'site_settings': {}}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)