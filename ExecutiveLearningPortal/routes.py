from flask import render_template, request, redirect, url_for, flash, jsonify
from main import app
from data.programmes import get_all_programmes, get_programme_by_id, get_programmes_by_category, get_programmes_by_industry, LEARNING_PATHWAYS, INDUSTRIES
from admin.models import db, ContactSubmission, ContentSection

@app.route('/')
def index():
    """Home page with clear messaging and journey builder CTA"""
    # Get dynamic content sections for home page
    hero_section = ContentSection.query.filter_by(page='home', section_name='hero', is_active=True).first()
    features_sections = ContentSection.query.filter_by(page='home', section_name='features', is_active=True).order_by(ContentSection.order_index).all()
    
    return render_template('index.html', hero_section=hero_section, features_sections=features_sections)

@app.route('/programmes')
def programmes():
    """Browse all programmes with filtering options"""
    category = request.args.get('category', 'all')
    industry = request.args.get('industry', 'all')
    
    if category != 'all':
        programmes = get_programmes_by_category(category)
    elif industry != 'all':
        programmes = get_programmes_by_industry(industry)
    else:
        programmes = get_all_programmes()
    
    return render_template('programmes.html', 
                         programmes=programmes,
                         categories=LEARNING_PATHWAYS,
                         industries=INDUSTRIES,
                         selected_category=category,
                         selected_industry=industry)

@app.route('/programme/<programme_id>')
def programme_detail(programme_id):
    """Individual programme details page"""
    programme = get_programme_by_id(programme_id)
    if not programme:
        flash('Programme not found', 'error')
        return redirect(url_for('programmes'))
    
    return render_template('programme_detail.html', programme=programme)

@app.route('/journey-builder')
def journey_builder():
    """Interactive learning journey builder"""
    return render_template('journey_builder.html', 
                         pathways=LEARNING_PATHWAYS,
                         industries=INDUSTRIES)

@app.route('/recommend-programmes', methods=['POST'])
def recommend_programmes():
    """API endpoint to recommend programmes based on user input"""
    role = request.form.get('role', '')
    industry = request.form.get('industry', '')
    experience = request.form.get('experience', '')
    goals = request.form.getlist('goals')
    
    # Simple recommendation logic based on role and industry
    recommended = []
    all_programmes = get_all_programmes()
    
    # Filter by industry if specified
    if industry and industry != 'all':
        candidates = [p for p in all_programmes if industry.lower() in p.get('focus', '').lower() or 
                     industry.lower() in p.get('target_audience', '').lower()]
    else:
        candidates = all_programmes
    
    # Filter by role/experience level
    for programme in candidates:
        target_audience = programme.get('target_audience', '').lower()
        
        # Match senior roles with executive programmes
        if 'senior' in role.lower() or 'executive' in role.lower() or 'c-suite' in role.lower():
            if programme.get('category') == 'senior_executive':
                recommended.append(programme)
        # Match mid-level with micro-credentials
        elif 'mid' in role.lower() or 'manager' in role.lower():
            if programme.get('category') in ['micro_credentials', 'senior_executive']:
                recommended.append(programme)
        # Early career gets micro-credentials
        elif 'early' in role.lower() or 'junior' in role.lower():
            if programme.get('category') == 'micro_credentials':
                recommended.append(programme)
        else:
            # Default recommendation
            recommended.append(programme)
    
    # Limit to top 6 recommendations
    recommended = recommended[:6]
    
    return render_template('journey_builder.html', 
                         pathways=LEARNING_PATHWAYS,
                         industries=INDUSTRIES,
                         recommended_programmes=recommended,
                         user_selections={
                             'role': role,
                             'industry': industry,
                             'experience': experience,
                             'goals': goals
                         })

@app.route('/about')
def about():
    """About page with company information and values"""
    # Get dynamic content sections for about page
    about_sections = ContentSection.query.filter_by(page='about', is_active=True).order_by(ContentSection.order_index).all()
    return render_template('about.html', about_sections=about_sections)

@app.route('/contact')
def contact():
    """Contact page for enquiries"""
    # Get dynamic content sections for contact page
    contact_sections = ContentSection.query.filter_by(page='contact', is_active=True).order_by(ContentSection.order_index).all()
    return render_template('contact.html', contact_sections=contact_sections)

@app.route('/submit-enquiry', methods=['POST'])
def submit_enquiry():
    """Handle contact form submissions"""
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    company = request.form.get('company')
    role = request.form.get('role')
    programme_interest = request.form.get('programme_interest')
    message = request.form.get('message')
    
    # Save to database
    try:
        submission = ContactSubmission(
            name=name,
            email=email,
            phone=phone,
            company=company,
            role=role,
            programme_interest=programme_interest,
            message=message,
            status='new'
        )
        db.session.add(submission)
        db.session.commit()
        
        flash(f'Thank you {name}! Your enquiry has been submitted. We will contact you within 24 hours.', 'success')
        app.logger.info(f'New enquiry from {name} ({email}) - Interest: {programme_interest}')
        
    except Exception as e:
        db.session.rollback()
        app.logger.error(f'Error saving enquiry: {str(e)}')
        flash('There was an error submitting your enquiry. Please try again.', 'error')
    
    return redirect(url_for('contact'))

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('base.html', 
                         title='Page Not Found',
                         content='<div class="container"><div class="row"><div class="col-md-8 mx-auto text-center"><h1>404 - Page Not Found</h1><p>The page you are looking for does not exist.</p><a href="/" class="btn btn-primary">Return Home</a></div></div></div>'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('base.html',
                         title='Server Error',
                         content='<div class="container"><div class="row"><div class="col-md-8 mx-auto text-center"><h1>500 - Server Error</h1><p>An internal server error occurred. Please try again later.</p><a href="/" class="btn btn-primary">Return Home</a></div></div></div>'), 500