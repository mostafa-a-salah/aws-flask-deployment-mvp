from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.utils import secure_filename
import os
import json
from datetime import datetime
from .models import (db, User, ContactSubmission, ContentSection, MediaFile, 
                    SiteSettings, BlogPost, Programme)
from .auth import login_required, admin_required, authenticate_user, create_admin_user
from .utils import allowed_file, save_uploaded_file, get_site_setting, update_site_setting

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = authenticate_user(username, password)
        if user and user.is_admin:
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('admin.dashboard'))
        else:
            flash('Invalid credentials or insufficient permissions.', 'error')
    
    return render_template('admin/login.html')

@admin_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@admin_bp.route('/')
@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    # Get dashboard statistics
    stats = {
        'total_submissions': ContactSubmission.query.count(),
        'new_submissions': ContactSubmission.query.filter_by(status='new').count(),
        'total_programmes': Programme.query.filter_by(is_active=True).count(),
        'total_blog_posts': BlogPost.query.count(),
        'published_posts': BlogPost.query.filter_by(status='published').count(),
        'total_media_files': MediaFile.query.count(),
        'total_content_sections': ContentSection.query.filter_by(is_active=True).count()
    }
    
    # Recent submissions
    recent_submissions = ContactSubmission.query.order_by(
        ContactSubmission.created_at.desc()
    ).limit(5).all()
    
    return render_template('admin/dashboard.html', stats=stats, recent_submissions=recent_submissions)

# Contact Submissions Management
@admin_bp.route('/submissions')
@admin_required
def submissions():
    page = request.args.get('page', 1, type=int)
    status_filter = request.args.get('status', 'all')
    
    query = ContactSubmission.query
    if status_filter != 'all':
        query = query.filter_by(status=status_filter)
    
    submissions = query.order_by(ContactSubmission.created_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    
    return render_template('admin/submissions.html', submissions=submissions, status_filter=status_filter)

@admin_bp.route('/submissions/<int:submission_id>')
@admin_required
def submission_detail(submission_id):
    submission = ContactSubmission.query.get_or_404(submission_id)
    return render_template('admin/submission_detail.html', submission=submission)

@admin_bp.route('/submissions/<int:submission_id>/update', methods=['POST'])
@admin_required
def update_submission(submission_id):
    submission = ContactSubmission.query.get_or_404(submission_id)
    submission.status = request.form.get('status')
    submission.notes = request.form.get('notes')
    
    try:
        db.session.commit()
        flash('Submission updated successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error updating submission: {str(e)}', 'error')
    
    return redirect(url_for('admin.submission_detail', submission_id=submission_id))

# Content Management
@admin_bp.route('/content')
@admin_required
def content():
    page_filter = request.args.get('page_filter', 'all')
    
    query = ContentSection.query
    if page_filter != 'all':
        query = query.filter_by(page=page_filter)
    
    sections = query.order_by(ContentSection.page, ContentSection.order_index).all()
    
    pages = ['home', 'about', 'programmes', 'contact', 'journey_builder']
    
    return render_template('admin/content.html', sections=sections, pages=pages, page_filter=page_filter)

@admin_bp.route('/content/add', methods=['GET', 'POST'])
@admin_required
def add_content():
    if request.method == 'POST':
        section = ContentSection(
            page=request.form.get('page'),
            section_name=request.form.get('section_name'),
            title=request.form.get('title'),
            subtitle=request.form.get('subtitle'),
            content=request.form.get('content'),
            image_url=request.form.get('image_url'),
            order_index=int(request.form.get('order_index', 0)),
            is_active=bool(request.form.get('is_active'))
        )
        
        try:
            db.session.add(section)
            db.session.commit()
            flash('Content section added successfully!', 'success')
            return redirect(url_for('admin.content'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding content: {str(e)}', 'error')
    
    pages = ['home', 'about', 'programmes', 'contact', 'journey_builder']
    return render_template('admin/content_form.html', pages=pages)

@admin_bp.route('/content/<int:section_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_content(section_id):
    section = ContentSection.query.get_or_404(section_id)
    
    if request.method == 'POST':
        section.page = request.form.get('page')
        section.section_name = request.form.get('section_name')
        section.title = request.form.get('title')
        section.subtitle = request.form.get('subtitle')
        section.content = request.form.get('content')
        section.image_url = request.form.get('image_url')
        section.order_index = int(request.form.get('order_index', 0))
        section.is_active = bool(request.form.get('is_active'))
        section.updated_at = datetime.utcnow()
        
        try:
            db.session.commit()
            flash('Content section updated successfully!', 'success')
            return redirect(url_for('admin.content'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating content: {str(e)}', 'error')
    
    pages = ['home', 'about', 'programmes', 'contact', 'journey_builder']
    return render_template('admin/content_form.html', section=section, pages=pages)

@admin_bp.route('/content/<int:section_id>/delete', methods=['POST'])
@admin_required
def delete_content(section_id):
    section = ContentSection.query.get_or_404(section_id)
    
    try:
        db.session.delete(section)
        db.session.commit()
        flash('Content section deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting content: {str(e)}', 'error')
    
    return redirect(url_for('admin.content'))

# Media Management
@admin_bp.route('/media')
@admin_required
def media():
    page = request.args.get('page', 1, type=int)
    file_type = request.args.get('type', 'all')
    
    query = MediaFile.query
    if file_type != 'all':
        query = query.filter_by(file_type=file_type)
    
    media_files = query.order_by(MediaFile.uploaded_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    
    return render_template('admin/media.html', media_files=media_files, file_type=file_type)

@admin_bp.route('/media/upload', methods=['POST'])
@admin_required
def upload_media():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': 'No file selected'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'message': 'No file selected'})
    
    if file and allowed_file(file.filename):
        try:
            file_info = save_uploaded_file(file)
            
            media_file = MediaFile(
                filename=file_info['filename'],
                original_filename=file_info['original_filename'],
                file_path=file_info['file_path'],
                file_type=file_info['file_type'],
                file_size=file_info['file_size'],
                description=request.form.get('description', '')
            )
            
            db.session.add(media_file)
            db.session.commit()
            
            return jsonify({
                'success': True,
                'message': 'File uploaded successfully',
                'file_url': file_info['url']
            })
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'message': f'Upload failed: {str(e)}'})
    
    return jsonify({'success': False, 'message': 'Invalid file type'})

@admin_bp.route('/media/<int:file_id>/delete', methods=['POST'])
@admin_required
def delete_media(file_id):
    media_file = MediaFile.query.get_or_404(file_id)
    
    try:
        # Delete physical file
        if os.path.exists(media_file.file_path):
            os.remove(media_file.file_path)
        
        db.session.delete(media_file)
        db.session.commit()
        flash('Media file deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting media file: {str(e)}', 'error')
    
    return redirect(url_for('admin.media'))

# Site Settings & Theme Management
@admin_bp.route('/settings')
@admin_required
def settings():
    settings = SiteSettings.query.all()
    settings_dict = {s.setting_key: s for s in settings}
    
    # Default settings if they don't exist
    default_settings = {
        'site_title': 'ESBE - Everest School of Business and Economics',
        'primary_color': '#0d6efd',
        'secondary_color': '#198754',
        'accent_color': '#ffc107',
        'success_color': '#198754',
        'warning_color': '#ffc107',
        'danger_color': '#dc3545',
        'info_color': '#0dcaf0',
        'light_color': '#f8f9fa',
        'dark_color': '#212529',
        'font_family': 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif',
        'logo_url': '/static/images/logo.png',
        'contact_email': 'info@esbe.edu',
        'contact_phone': '+971 XX XXX XXXX',
        'footer_text': 'Empowering MENA Leaders to Engineer Sustainable Economic Growth'
    }
    
    return render_template('admin/settings.html', settings_dict=settings_dict, default_settings=default_settings)

@admin_bp.route('/settings/update', methods=['POST'])
@admin_required
def update_settings():
    try:
        for key, value in request.form.items():
            if key.startswith('setting_'):
                setting_key = key.replace('setting_', '')
                setting_type = 'color' if 'color' in setting_key else 'text'
                update_site_setting(setting_key, value, setting_type)
        
        db.session.commit()
        flash('Settings updated successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error updating settings: {str(e)}', 'error')
    
    return redirect(url_for('admin.settings'))

# API Endpoints
@admin_bp.route('/api/media-list')
@admin_required
def api_media_list():
    media_files = MediaFile.query.filter_by(file_type='image').all()
    return jsonify([{
        'id': f.id,
        'filename': f.filename,
        'url': f'/static/uploads/{f.filename}',
        'description': f.description
    } for f in media_files])

# Initialize admin user (run once)
@admin_bp.route('/init-admin', methods=['GET', 'POST'])
def init_admin():
    # Check if admin already exists
    if User.query.filter_by(is_admin=True).first():
        flash('Admin user already exists.', 'info')
        return redirect(url_for('admin.login'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
        else:
            success, message = create_admin_user(username, email, password)
            if success:
                flash(message, 'success')
                return redirect(url_for('admin.login'))
            else:
                flash(message, 'error')
    
    return render_template('admin/init_admin.html')