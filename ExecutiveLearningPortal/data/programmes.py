"""
Programme data structure based on ESBE company profile and programme structures
"""

LEARNING_PATHWAYS = {
    'senior_executive': {
        'name': 'UK Senior Executive Education',
        'tagline': 'Lead Transformation at Scale',
        'description': 'Elevating leadership excellence for MENA\'s sustainable transformation.',
        'target': 'C-suite executives, decision makers, policymakers, and board members'
    },
    'micro_credentials': {
        'name': 'UK Micro-Credentials',
        'tagline': 'Skill Up, Stand Out',
        'description': 'Accelerate Your Learning. Expand Your Horizons.',
        'target': 'Early-career and Mid-career professionals seeking rapid upskilling'
    },
    'corporate': {
        'name': 'Corporate Development Programmes',
        'tagline': 'Build Your Edge',
        'description': 'Tailored solutions for organizational transformation.',
        'target': 'Organizations and teams'
    }
}

INDUSTRIES = {
    'financial': 'Financial Services',
    'healthcare': 'Healthcare & Medical',
    'energy': 'Energy & Sustainability',
    'general': 'Cross-Sector Leadership'
}

PROGRAMMES_DATA = [
    # Senior Executive Education - Transformation Leadership Line
    {
        'id': 'cdts',
        'title': 'Certified Digital Transformation Strategist (CDTS)',
        'short_description': 'Empowers leaders with tools and strategies to lead digital innovation using AI, big data, and governance frameworks.',
        'category': 'senior_executive',
        'line': 'transformation_leadership',
        'industry': 'general',
        'target_audience': 'C-Suite Executives, Board Members, Risk & Compliance Professionals, Internal Auditors, Business Unit Heads, Finance & Accounting Leaders, Consultants, and Aspiring Digital Transformation Strategists',
        'delivery': 'Flexible options: Online or In-Person',
        'focus': 'Strategic leadership for navigating digital disruption, diversifying reward, empowering human capital, and inclusive growth',
        'modules': [
            'Foundations of GRC',
            'Technological Transformations and the 4IR',
            'Data-Driven Decision Making and AI Integration',
            'Strategic Data Valuation and Monetisation',
            'Digital Transformation & National Strategies',
            'Advanced Digital Governance & Security Strategies'
        ],
        'overview': 'This dynamic programme equips participants with the critical tools and frameworks needed to harness the power of digital governance, big data, AI, and emerging technologies. Focused on value creation, risk management, and compliance, it prepares leaders to turn digital innovation into sustainable business strategies.'
    },
    {
        'id': 'cffo',
        'title': 'Certified Financial Fluency Officer (CFFO)',
        'short_description': 'Master advanced financial tools, budgeting strategies, and performance-driven insights for sustainable success.',
        'category': 'senior_executive',
        'line': 'transformation_leadership',
        'industry': 'financial',
        'target_audience': 'Senior Executives, Finance Professionals, Corporate Strategists, Aspiring Leaders in Finance, and Specialized Finance Professionals',
        'delivery': 'Flexible options: Online or In-Person',
        'focus': 'Advanced financial analysis, strategic planning, and sustainable growth',
        'modules': [
            'Strategic Financial Decision-Making',
            'Advanced Financial Analysis',
            'Budgeting & Investment Appraisal',
            'Financial Resilience & Sustainable Growth',
            'Innovative Financing Options',
            'Strategic Planning & KPI Integration'
        ],
        'overview': 'This transformative programme equips leaders with advanced financial tools, strategic insights, and the confidence to drive sustainable business success. Through workshops, real-world cases, and expert sessions, participants gain mastery in budgeting, analysis, and risk management.'
    },
    {
        'id': 'cfip',
        'title': 'Certified Fintech Mastery for Inclusion Professional (CFIP)',
        'short_description': 'Equips professionals with tools to leverage fintech for financial inclusion and equity.',
        'category': 'senior_executive',
        'line': 'transformation_leadership',
        'industry': 'financial',
        'target_audience': 'Bank Executives, CTOs, Government Officials, Venture Capitalists, Consultants, Sustainability Officers, Fintech Entrepreneurs, NGO Leaders, Financial Analysts, and Consultants',
        'delivery': 'Flexible options: Online or In-Person',
        'focus': 'Financial inclusion, fintech innovation, and digital transformation',
        'modules': [
            'Financial Services Landscape',
            'Fintech Entrepreneurship and Innovation',
            'Fintech Operations',
            'Fintech Security and Regulations',
            'Digital Banking Transformation',
            'Financial Inclusion and Financial Literacy',
            'Financial Inclusion and Economic Development',
            'AI in Fintech'
        ],
        'overview': 'This programme is designed for forward-thinking professionals, policymakers, and innovators. It provides practical, future-ready skills to design and implement inclusive financial systems using digital payment ecosystems, mobile banking, blockchain, and RegTech.'
    },
    {
        'id': 'cieo',
        'title': 'Certified Investment Engineering Officer (CIEO)',
        'short_description': 'Equips professionals to structure investment vehicles and drive business growth.',
        'category': 'senior_executive',
        'line': 'transformation_leadership',
        'industry': 'financial',
        'target_audience': 'Professionals in investment, C-suite executives, visionary business owners, corporate finance specialists, and policymakers',
        'delivery': 'Flexible options: Online or Bootcamp',
        'focus': 'Investment structuring, financial engineering, and business development',
        'modules': [
            'Introduction to Investment Structuring',
            'Understanding the Investment Landscape',
            'Legal and Regulatory Framework',
            'Equity and Debt Structuring',
            'Hybrid Instruments',
            'Corporate Structuring for Investments',
            'Financial Structuring Considerations',
            'Advanced Structuring Techniques',
            'Business and Process Engineering',
            'Case Studies and Applications'
        ],
        'overview': 'This cutting-edge programme prepares participants to engineer financial solutions, covering equity structuring, debt instruments, and deal design. It blends analytical rigour with practical application.'
    },
    {
        'id': 'clrse',
        'title': 'Certified Leadership Resilience and Sustainability Executive (CLRSE)',
        'short_description': 'Develops leaders to thrive under pressure, drive change, and lead with purpose.',
        'category': 'senior_executive',
        'line': 'transformation_leadership',
        'industry': 'general',
        'target_audience': 'Change agents, sustainability officers, policymakers, nonprofit leaders, project managers, entrepreneurs, business owners',
        'delivery': '32 hours online sessions + 16 hours onsite workshop',
        'focus': 'Leadership resilience, crisis management, and sustainable decision-making',
        'modules': [
            'Developing Leadership Skills',
            'Leadership Resilience',
            'Chesley Sullenberger\'s Model - Leadership in Crisis',
            'AI in Leadership',
            'Sustainability in Leadership'
        ],
        'overview': 'Blends leadership theory with execution, foresight, crisis management, and AI integration. Focuses on change navigation, team resilience, and sustainable decision-making.'
    },
    {
        'id': 'copp',
        'title': 'Certified Organisational Psychology Professional (COPP)',
        'short_description': 'Leverages psychological principles to enhance workplace dynamics and leadership.',
        'category': 'senior_executive',
        'line': 'transformation_leadership',
        'industry': 'general',
        'target_audience': 'Team leaders, C-suite executives, change agents, educators, senior managers, aspiring leaders, project managers, organisational consultants',
        'delivery': 'Flexible options: Online or In-Person',
        'focus': 'Organizational psychology, workplace dynamics, and leadership development',
        'modules': [
            'Foundations of Industrial and Organisational Psychology',
            'Social Dynamics in Organizations',
            'Optimizing Workplace Environment',
            'Creating Healthy and Harmonious Work Environments',
            'Promoting Equity, Ethics, and Social Awareness'
        ],
        'overview': 'This programme offers a comprehensive exploration of the psychological principles that shape workplace dynamics, leadership, and organisational culture.'
    },
    # Sustainability Transition Line
    {
        'id': 'csds',
        'title': 'Certified Sustainable Development Specialist (CSDS)',
        'short_description': 'Equips professionals to lead sustainability initiatives across sectors.',
        'category': 'senior_executive',
        'line': 'sustainability_transition',
        'industry': 'energy',
        'target_audience': 'Professionals, managers, and executives across sectors leading sustainability efforts',
        'delivery': 'Flexible options: Online or In-Person',
        'focus': 'Sustainable development, environmental stewardship, and global challenges',
        'modules': [
            'Introduction to Sustainable Development Principles',
            'Planetary Boundaries and Global Sustainability',
            'Environmental-Economic Dynamics in Sustainable Development',
            'Foundations of Social Equity and Sustainable Governance',
            'Achieving the Sustainable Development Goals (SDGs)',
            'Strategic Pathways for Global Sustainability',
            'Measuring Progress Towards the SDGs',
            'Resilience Thinking in Sustainable Development',
            'Sustainable Business Strategy and Corporate Responsibility',
            'Visionary Leadership for Global Sustainability'
        ],
        'overview': 'Provides an in-depth curriculum on economic and social sustainability, environmental stewardship, and leadership for global challenges.'
    },
    {
        'id': 'csls',
        'title': 'Certified SDGs Leadership Strategist (CSLS)',
        'short_description': 'Trains professionals to lead transformative change aligned with SDGs.',
        'category': 'senior_executive',
        'line': 'sustainability_transition',
        'industry': 'general',
        'target_audience': 'Senior executives, ESG and CSR professionals, policymakers, NGO leaders, sustainability consultants, change agents',
        'delivery': 'Flexible options: Online or In-Person',
        'focus': 'SDGs alignment, transformative leadership, and sustainable development',
        'modules': [
            'Strategic Goal Alignment with Global Sustainability',
            'Bridging Societal Divides for Sustainable Progress',
            'Ethical Leadership for Inclusive Development',
            'Navigating Multilateralism in the Sustainability Era',
            'Legacy Building for Sustainable Leadership',
            'Instigating Organizational Change for a Sustainable Future'
        ],
        'overview': 'Provides tools and insights needed to lead and support transformative initiatives that align with global sustainability goals.'
    },
    {
        'id': 'csbs',
        'title': 'Certified ESG Sustainable Banking Specialist (CSBS)',
        'short_description': 'Equips banking professionals to integrate ESG into operations.',
        'category': 'senior_executive',
        'line': 'sustainability_transition',
        'industry': 'financial',
        'target_audience': 'New Bank Employees and Mid-Level Professionals',
        'delivery': 'Flexible options: Online or In-Person',
        'focus': 'ESG integration in banking, sustainable finance practices',
        'modules': [
            'Introduction to Sustainability in Banking and ESG',
            'Sustainable Finance and Sustainable Development',
            'Inclusion of Individuals and Businesses',
            'Green Digital Skills',
            'Educate Your Customer',
            'ESG Strategies for Global Banking Operations',
            'ESG Disclosure and Reporting',
            'ESG Integration in Financial Analysis',
            'Aligning ESG with SDGs',
            'ESG Considerations for Banks',
            'Future Trends in Sustainable Banking'
        ],
        'overview': 'Covers ESG principles and their integration into banking practices with a focus on sustainability goals.'
    },
    {
        'id': 'csbp',
        'title': 'Certified ESG Sustainable Banking Professional (CSBP)',
        'short_description': 'Trains professionals to manage ESG risk and reporting in banking.',
        'category': 'senior_executive',
        'line': 'sustainability_transition',
        'industry': 'financial',
        'target_audience': 'Team Leaders & Supervisors in banking and finance',
        'delivery': 'Flexible options: Online or In-Person',
        'focus': 'ESG risk management, climate risks, sustainable finance practices',
        'modules': [
            'Understanding Financial Risks of ESG',
            'ESG Risks in the Banking Industry'
        ],
        'overview': 'Covers ESG risk management, climate risks, sustainable finance practices, and change management strategies.'
    },
    # Micro-Credentials - Financial Sector
    {
        'id': 'ai_esg_due_diligence',
        'title': 'AI for ESG Due Diligence',
        'short_description': 'AI-driven ESG analysis for critical investment decisions.',
        'category': 'micro_credentials',
        'line': 'financial',
        'industry': 'financial',
        'target_audience': 'Financial analysts, investment professionals, ESG officers',
        'delivery': '8 weeks online',
        'focus': 'AI applications in ESG analysis and investment decision-making',
        'modules': ['AI fundamentals', 'ESG data analysis', 'Investment applications', 'Risk assessment'],
        'overview': 'Learn to leverage AI for comprehensive ESG due diligence in investment decisions.',
        'duration': '8 weeks'
    },
    {
        'id': 'green_sukuk',
        'title': 'ESG & Green Sukuk Structuring',
        'short_description': 'Master sustainable Islamic bond structuring for green finance.',
        'category': 'micro_credentials',
        'line': 'financial',
        'industry': 'financial',
        'target_audience': 'Islamic finance professionals, investment bankers, sustainability officers',
        'delivery': '6 weeks online',
        'focus': 'Sukuk structuring for sustainable finance applications',
        'modules': ['Islamic finance principles', 'Green sukuk structures', 'Regulatory compliance', 'Market applications'],
        'overview': 'Master the growing field of sustainable Islamic bonds (sukuk) for green finance initiatives.',
        'duration': '6 weeks'
    },
    {
        'id': 'esg_reporting',
        'title': 'ESG & Sustainability Reporting Systems (GRI, CSRD, ISSB)',
        'short_description': 'Master global ESG reporting frameworks and compliance.',
        'category': 'micro_credentials',
        'line': 'financial',
        'industry': 'general',
        'target_audience': 'Sustainability officers, compliance professionals, financial analysts',
        'delivery': '6 weeks online',
        'focus': 'Global ESG reporting standards and implementation',
        'modules': ['GRI standards', 'CSRD requirements', 'ISSB framework', 'Implementation strategies'],
        'overview': 'Comprehensive training on major global ESG reporting frameworks essential for compliance.',
        'duration': '6 weeks'
    },
    # Micro-Credentials - Healthcare Sector
    {
        'id': 'blockchain_pharma',
        'title': 'Blockchain for Pharmaceutical Supply Chains',
        'short_description': 'Ensure transparency and traceability in drug logistics.',
        'category': 'micro_credentials',
        'line': 'healthcare',
        'industry': 'healthcare',
        'target_audience': 'Pharmaceutical managers, supply chain professionals, healthcare administrators',
        'delivery': '6 weeks online',
        'focus': 'Blockchain applications for pharmaceutical supply chain transparency',
        'modules': ['Blockchain fundamentals', 'Supply chain applications', 'Regulatory considerations', 'Implementation'],
        'overview': 'Learn to implement blockchain solutions for pharmaceutical supply chain transparency and compliance.',
        'duration': '6 weeks'
    },
    {
        'id': 'medical_waste_innovation',
        'title': 'Medical Waste-to-Value Innovation Professional',
        'short_description': 'Transform healthcare waste into value through circular economy principles.',
        'category': 'micro_credentials',
        'line': 'healthcare',
        'industry': 'healthcare',
        'target_audience': 'Healthcare sustainability officers, facility managers, environmental coordinators',
        'delivery': '5 weeks online',
        'focus': 'Circular economy applications in healthcare waste management',
        'modules': ['Waste assessment', 'Value creation strategies', 'Regulatory compliance', 'Implementation planning'],
        'overview': 'Develop innovative approaches to transform medical waste into valuable resources through circular economy principles.',
        'duration': '5 weeks'
    },
    # Micro-Credentials - Energy Sector
    {
        'id': 'green_hydrogen',
        'title': 'Green Hydrogen Energy Systems Professional',
        'short_description': 'Master green hydrogen technology for decarbonization.',
        'category': 'micro_credentials',
        'line': 'energy',
        'industry': 'energy',
        'target_audience': 'Energy professionals, project managers, sustainability officers',
        'delivery': '6 weeks online',
        'focus': 'Green hydrogen systems for industrial decarbonization',
        'modules': ['Hydrogen fundamentals', 'Production technologies', 'Applications', 'Project development'],
        'overview': 'Comprehensive training on green hydrogen systems crucial for achieving net-zero goals in heavy industry and transport.',
        'duration': '6 weeks'
    },
    {
        'id': 'grid_modernisation',
        'title': 'Grid Modernisation and Smart Energy Systems',
        'short_description': 'Essential skills for integrating renewables and managing distributed energy.',
        'category': 'micro_credentials',
        'line': 'energy',
        'industry': 'energy',
        'target_audience': 'Grid operators, energy engineers, utility professionals',
        'delivery': '6 weeks online',
        'focus': 'Smart grid technologies and renewable energy integration',
        'modules': ['Grid fundamentals', 'Smart technologies', 'Renewable integration', 'System management'],
        'overview': 'Learn essential skills for modernizing electrical grids to accommodate renewable energy and distributed systems.',
        'duration': '6 weeks'
    }
]

def get_all_programmes():
    """Return all programmes"""
    return PROGRAMMES_DATA

def get_programme_by_id(programme_id):
    """Get a specific programme by ID"""
    for programme in PROGRAMMES_DATA:
        if programme['id'] == programme_id:
            return programme
    return None

def get_programmes_by_category(category):
    """Get programmes filtered by category"""
    return [p for p in PROGRAMMES_DATA if p['category'] == category]

def get_programmes_by_industry(industry):
    """Get programmes filtered by industry"""
    return [p for p in PROGRAMMES_DATA if p['industry'] == industry]

def get_programmes_by_line(line):
    """Get programmes filtered by programme line"""
    return [p for p in PROGRAMMES_DATA if p.get('line') == line]
