import os
import uuid
from werkzeug.utils import secure_filename
from flask import current_app
from .models import SiteSettings, db

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'doc', 'docx', 'svg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_uploaded_file(file):
    """Save uploaded file and return file info"""
    if not file or not allowed_file(file.filename):
        raise ValueError("Invalid file type")
    
    # Create uploads directory if it doesn't exist
    upload_dir = os.path.join(current_app.static_folder, 'uploads')
    os.makedirs(upload_dir, exist_ok=True)
    
    # Generate unique filename
    original_filename = secure_filename(file.filename)
    file_extension = original_filename.rsplit('.', 1)[1].lower()
    unique_filename = f"{uuid.uuid4().hex}.{file_extension}"
    
    file_path = os.path.join(upload_dir, unique_filename)
    file.save(file_path)
    
    # Determine file type
    file_type = 'image' if file_extension in {'png', 'jpg', 'jpeg', 'gif', 'svg'} else 'document'
    
    # Get file size
    file_size = os.path.getsize(file_path)
    
    return {
        'filename': unique_filename,
        'original_filename': original_filename,
        'file_path': file_path,
        'file_type': file_type,
        'file_size': file_size,
        'url': f'/static/uploads/{unique_filename}'
    }

def get_site_setting(key, default=None):
    """Get site setting value"""
    setting = SiteSettings.query.filter_by(setting_key=key).first()
    return setting.setting_value if setting else default

def update_site_setting(key, value, setting_type='text', description=None):
    """Update or create site setting"""
    setting = SiteSettings.query.filter_by(setting_key=key).first()
    if setting:
        setting.setting_value = value
        setting.setting_type = setting_type
        if description:
            setting.description = description
    else:
        setting = SiteSettings(
            setting_key=key,
            setting_value=value,
            setting_type=setting_type,
            description=description
        )
        db.session.add(setting)
    
    return setting

def get_all_settings():
    """Get all site settings as a dictionary"""
    settings = SiteSettings.query.all()
    return {s.setting_key: s.setting_value for s in settings}