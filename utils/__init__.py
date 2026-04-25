"""
Data loader utility for populating database with initial data
"""

import json
import os
from models import db, College, Program, Career, EntranceExam, StreamMapping


def load_colleges_data():
    """Load colleges data from JSON file"""
    
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'colleges_data.json')
    
    if not os.path.exists(data_path):
        print(f"❌ File not found: {data_path}")
        return False
    
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        colleges_data = data.get('colleges', [])
        loaded_count = 0
        
        for college_data in colleges_data:
            # Check if college already exists
            existing = College.query.filter_by(name=college_data['name']).first()
            if existing:
                print(f"⚠️  College already exists: {college_data['name']}")
                continue
            
            # Create new college
            college = College(
                name=college_data['name'],
                college_type=college_data.get('college_type'),
                city=college_data.get('city'),
                state=college_data.get('state', 'Jammu & Kashmir'),
                established_year=college_data.get('established_year'),
                affiliation=college_data.get('affiliation'),
                streams=college_data.get('streams'),
                degree_type=college_data.get('degree_type'),
                duration_years=college_data.get('duration_years'),
                total_fees=college_data.get('total_fees'),
                annual_fees=college_data.get('annual_fees'),
                admission_type=college_data.get('admission_type'),
                cutoff_percentage=college_data.get('cutoff_percentage'),
                branches=college_data.get('branches'),
                subjects=college_data.get('subjects'),
                facilities=college_data.get('facilities'),
                contact_phone=college_data.get('contact_phone'),
                contact_email=college_data.get('contact_email'),
                website=college_data.get('website'),
                description=college_data.get('description')
            )
            
            db.session.add(college)
            loaded_count += 1
        
        db.session.commit()
        print(f"✅ Successfully loaded {loaded_count} colleges")
        return True
        
    except Exception as e:
        print(f"❌ Error loading colleges: {str(e)}")
        db.session.rollback()
        return False


def load_careers_data():
    """Load careers data"""
    
    careers = [
        {
            'name': 'Software Engineer',
            'stream': 'Science',
            'avg_salary': 600000,
            'description': 'Develops and maintains software applications',
            'required_skills': ['Programming', 'Problem Solving', 'Communication'],
            'job_sectors': ['IT', 'Technology', 'Finance'],
            'growth_rate': 'High',
            'education_required': 'B.Tech / BCA'
        },
        {
            'name': 'Data Scientist',
            'stream': 'Science',
            'avg_salary': 750000,
            'description': 'Analyzes large datasets and builds predictive models',
            'required_skills': ['Statistics', 'Programming', 'Machine Learning'],
            'job_sectors': ['IT', 'Finance', 'Healthcare'],
            'growth_rate': 'Very High',
            'education_required': 'B.Tech / M.Sc.'
        },
        {
            'name': 'Civil Engineer',
            'stream': 'Science',
            'avg_salary': 400000,
            'description': 'Plans and oversees construction projects',
            'required_skills': ['Design', 'Project Management', 'Technical Knowledge'],
            'job_sectors': ['Construction', 'Government', 'Infrastructure'],
            'growth_rate': 'Medium',
            'education_required': 'B.Tech (Civil)'
        },
        {
            'name': 'Lawyer',
            'stream': 'Arts',
            'avg_salary': 500000,
            'description': 'Provides legal advice and represents clients',
            'required_skills': ['Legal Knowledge', 'Communication', 'Negotiation'],
            'job_sectors': ['Law Firm', 'Government', 'Corporate'],
            'growth_rate': 'High',
            'education_required': 'LL.B / B.A. LL.B'
        },
        {
            'name': 'Teacher',
            'stream': 'Arts',
            'avg_salary': 300000,
            'description': 'Educates students in schools',
            'required_skills': ['Communication', 'Patience', 'Subject Expertise'],
            'job_sectors': ['Education', 'Schools', 'Coaching'],
            'growth_rate': 'Medium',
            'education_required': 'B.Ed'
        },
        {
            'name': 'Pharmacist',
            'stream': 'Science',
            'avg_salary': 350000,
            'description': 'Prepares and dispenses medicines',
            'required_skills': ['Chemistry', 'Patient Care', 'Communication'],
            'job_sectors': ['Pharmacy', 'Hospital', 'Pharmaceutical'],
            'growth_rate': 'Medium',
            'education_required': 'B.Pharm'
        },
        {
            'name': 'Business Analyst',
            'stream': 'Commerce',
            'avg_salary': 550000,
            'description': 'Analyzes business requirements and recommends solutions',
            'required_skills': ['Analysis', 'Communication', 'Technical Knowledge'],
            'job_sectors': ['IT', 'Consulting', 'Finance'],
            'growth_rate': 'High',
            'education_required': 'BCA / B.Com'
        },
        {
            'name': 'Journalist',
            'stream': 'Arts',
            'avg_salary': 350000,
            'description': 'Researches and reports news',
            'required_skills': ['Writing', 'Research', 'Communication'],
            'job_sectors': ['Media', 'News Agency', 'Publishing'],
            'growth_rate': 'Medium',
            'education_required': 'B.A.'
        }
    ]
    
    try:
        for career_data in careers:
            existing = Career.query.filter_by(name=career_data['name']).first()
            if existing:
                continue
            
            career = Career(**career_data)
            db.session.add(career)
        
        db.session.commit()
        print(f"✅ Successfully loaded {len(careers)} careers")
        return True
        
    except Exception as e:
        print(f"❌ Error loading careers: {str(e)}")
        db.session.rollback()
        return False


def load_exams_data():
    """Load entrance exams data"""
    
    exams = [
        {
            'exam_name': 'JEE Main',
            'stream': 'Science',
            'exam_type': 'National',
            'description': 'Joint Entrance Examination for engineering colleges',
            'eligibility': '12th pass with PCM',
            'exam_duration': '3 hours',
            'total_marks': 300,
            'exam_fee': 1500,
            'official_website': 'https://jeemain.nta.ac.in',
            'colleges_accepting': ['NIT Srinagar', 'GCET Jammu', 'SMVDU Katra']
        },
        {
            'exam_name': 'JEE Advanced',
            'stream': 'Science',
            'exam_type': 'National',
            'description': 'Advanced entrance exam for IITs',
            'eligibility': 'JEE Main qualified',
            'exam_duration': '6 hours',
            'total_marks': 300,
            'exam_fee': 2800,
            'official_website': 'https://jeeadv.ac.in',
            'colleges_accepting': ['IIT Jammu']
        },
        {
            'exam_name': 'CLAT',
            'stream': 'Arts',
            'exam_type': 'National',
            'description': 'Common Law Admission Test',
            'eligibility': '12th pass',
            'exam_duration': '2 hours',
            'total_marks': 150,
            'exam_fee': 4000,
            'official_website': 'https://consortiumofnlus.ac.in',
            'colleges_accepting': ['University of Jammu', 'University of Kashmir', 'CUK']
        },
        {
            'exam_name': 'J&K B.Ed Entrance',
            'stream': 'Arts',
            'exam_type': 'State',
            'description': 'State level entrance for B.Ed programs',
            'eligibility': '12th pass or Graduate',
            'exam_duration': '2 hours',
            'total_marks': 100,
            'exam_fee': 500,
            'official_website': 'https://jammu.ac.in',
            'colleges_accepting': ['GCE Jammu', 'GCE Srinagar', 'TEC Ganderbal']
        }
    ]
    
    try:
        for exam_data in exams:
            existing = EntranceExam.query.filter_by(exam_name=exam_data['exam_name']).first()
            if existing:
                continue
            
            exam = EntranceExam(**exam_data)
            db.session.add(exam)
        
        db.session.commit()
        print(f"✅ Successfully loaded {len(exams)} entrance exams")
        return True
        
    except Exception as e:
        print(f"❌ Error loading exams: {str(e)}")
        db.session.rollback()
        return False


def initialize_database(app):
    """Initialize database with all data"""
    
    with app.app_context():
        print("\n🚀 Initializing database...\n")
        
        # Create tables
        print("📦 Creating database tables...")
        db.create_all()
        print("✅ Tables created\n")
        
        # Load data
        print("📥 Loading data...\n")
        load_colleges_data()
        load_careers_data()
        load_exams_data()
        
        print("\n✅ Database initialization complete!")


def clear_database(app):
    """Clear all data from database (use with caution)"""
    
    with app.app_context():
        print("\n⚠️  Clearing database...\n")
        db.drop_all()
        db.create_all()
        print("✅ Database cleared and reset\n")
