from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ContactSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    company = db.Column(db.String(100))
    role = db.Column(db.String(100))
    programme_interest = db.Column(db.String(100))
    message = db.Column(db.Text)
    status = db.Column(db.String(20), default='new')  # new, contacted, closed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)

class ContentSection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.String(50), nullable=False)  # home, about, programmes, etc.
    section_name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200))
    subtitle = db.Column(db.String(300))
    content = db.Column(db.Text)
    image_url = db.Column(db.String(300))
    order_index = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class MediaFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_type = db.Column(db.String(50))  # image, document, etc.
    file_size = db.Column(db.Integer)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.Text)

class SiteSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    setting_key = db.Column(db.String(100), unique=True, nullable=False)
    setting_value = db.Column(db.Text)
    setting_type = db.Column(db.String(50), default='text')  # text, color, boolean, json
    description = db.Column(db.String(300))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    excerpt = db.Column(db.Text)
    content = db.Column(db.Text)
    featured_image = db.Column(db.String(300))
    author = db.Column(db.String(100))
    status = db.Column(db.String(20), default='draft')  # draft, published
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published_at = db.Column(db.DateTime)

class Programme(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    short_description = db.Column(db.Text)
    overview = db.Column(db.Text)
    category = db.Column(db.String(50))
    industry = db.Column(db.String(50))
    target_audience = db.Column(db.Text)
    delivery = db.Column(db.String(200))
    focus = db.Column(db.Text)
    modules = db.Column(db.Text)  # JSON string
    duration = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def get_modules_list(self):
        if self.modules:
            try:
                return json.loads(self.modules)
            except:
                return []
        return []
    
    def set_modules_list(self, modules_list):
        self.modules = json.dumps(modules_list)