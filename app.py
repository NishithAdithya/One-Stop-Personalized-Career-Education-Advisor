from flask import Flask, render_template, request, redirect, url_for, session, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import json
import os
from datetime import datetime, timedelta
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'sih-career-advisor-2026-secret-key'

# Database Configuration
db_path = os.path.join(os.path.dirname(__file__), 'career_advisor.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Session configuration
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['SESSION_COOKIE_HTTPONLY'] = False
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_PATH'] = '/'
app.config['SESSION_REFRESH_EACH_REQUEST'] = True

@app.before_request
def before_request():
    """Ensure session is properly managed"""
    if 'user_id' in session:
        session.permanent = True
        app.permanent_session_lifetime = timedelta(days=7)
        session.modified = True

@app.after_request
def after_request(response):
    """Ensure session cookies are sent"""
    if 'user_id' in session:
        session.permanent = True
        app.permanent_session_lifetime = timedelta(days=7)
    return response

# ============ DATABASE MODELS ============

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    class_level = db.Column(db.String(10), nullable=False)
    stream = db.Column(db.String(50), default="Not Selected")
    phone = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    academic_percentage = db.Column(db.Float, default=0)
    selected_college = db.Column(db.String(200), nullable=True)
    selected_college_id = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    quiz_results = db.relationship('QuizResult', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class QuizResult(db.Model):
    __tablename__ = 'quiz_results'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    science_score = db.Column(db.Float, default=0)
    commerce_score = db.Column(db.Float, default=0)
    arts_score = db.Column(db.Float, default=0)
    vocational_score = db.Column(db.Float, default=0)
    recommended_stream = db.Column(db.String(50), nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)

DEMO_USERS = [
    {
        "id": 1,
        "email": "student@example.com",
        "password": "password123",
        "name": "Rahul Kumar",
        "class": "12",
        "stream": "Science",
        "phone": "9876543210",
        "state": "Jammu & Kashmir",
        "city": "Srinagar",
        "academic_percentage": 85
    },
    {
        "id": 2,
        "email": "artsstudent@example.com",
        "password": "password123",
        "name": "Priya Singh",
        "class": "10",
        "stream": "Arts",
        "phone": "8765432109",
        "state": "Jammu & Kashmir",
        "city": "Jammu",
        "academic_percentage": 78
    },
    {
        "id": 3,
        "email": "commerce@example.com",
        "password": "password123",
        "name": "Arjun Patel",
        "class": "11",
        "stream": "Commerce",
        "phone": "7654321098",
        "state": "Jammu & Kashmir",
        "city": "Leh",
        "academic_percentage": 82
    }
]

# ============ COMPREHENSIVE QUIZ QUESTIONS ============
QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "What do you enjoy doing most in your free time?",
        "options": [
            {"text": "Solving math problems and coding", "science": 4, "commerce": 1, "arts": 0, "vocational": 1},
            {"text": "Reading books and analyzing stories", "science": 0, "commerce": 1, "arts": 4, "vocational": 0},
            {"text": "Managing finances and planning budgets", "science": 1, "commerce": 4, "arts": 1, "vocational": 0},
            {"text": "Building things and fixing mechanical objects", "science": 2, "commerce": 0, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 2,
        "question": "Which subject comes easiest to you?",
        "options": [
            {"text": "Physics and Mathematics", "science": 4, "commerce": 1, "arts": 0, "vocational": 2},
            {"text": "History and Literature", "science": 0, "commerce": 0, "arts": 4, "vocational": 0},
            {"text": "Economics and Business Studies", "science": 1, "commerce": 4, "arts": 1, "vocational": 0},
            {"text": "Practical/Hands-on learning", "science": 1, "commerce": 0, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 3,
        "question": "Your career goal is to become:",
        "options": [
            {"text": "Engineer, Doctor, or Scientist", "science": 4, "commerce": 0, "arts": 0, "vocational": 1},
            {"text": "Lawyer, Journalist, or IAS Officer", "science": 0, "commerce": 1, "arts": 4, "vocational": 0},
            {"text": "Businessman, Accountant, or Banker", "science": 1, "commerce": 4, "arts": 1, "vocational": 0},
            {"text": "Skilled Technician or Tradesperson", "science": 1, "commerce": 0, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 4,
        "question": "How do you prefer to learn?",
        "options": [
            {"text": "Through experiments, labs, and theory", "science": 4, "commerce": 1, "arts": 0, "vocational": 2},
            {"text": "Through reading, discussions, and debates", "science": 0, "commerce": 1, "arts": 4, "vocational": 0},
            {"text": "Through case studies and real-world examples", "science": 1, "commerce": 4, "arts": 2, "vocational": 1},
            {"text": "Through hands-on projects and practical work", "science": 1, "commerce": 0, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 5,
        "question": "What matters most to you in a job?",
        "options": [
            {"text": "Innovation and research opportunities", "science": 4, "commerce": 0, "arts": 1, "vocational": 1},
            {"text": "Making social impact and helping people", "science": 1, "commerce": 1, "arts": 4, "vocational": 2},
            {"text": "Financial growth and business success", "science": 0, "commerce": 4, "arts": 0, "vocational": 1},
            {"text": "Stable income and job security", "science": 1, "commerce": 2, "arts": 1, "vocational": 4}
        ]
    },
    {
        "id": 6,
        "question": "How would you describe your analytical skills?",
        "options": [
            {"text": "Excellent with numbers and logic", "science": 4, "commerce": 4, "arts": 1, "vocational": 1},
            {"text": "Good at understanding people and ideas", "science": 0, "commerce": 1, "arts": 4, "vocational": 1},
            {"text": "Average - prefer practical application", "science": 1, "commerce": 1, "arts": 1, "vocational": 4},
            {"text": "Strong problem-solving abilities", "science": 4, "commerce": 2, "arts": 1, "vocational": 3}
        ]
    },
    {
        "id": 7,
        "question": "Which statement describes you best?",
        "options": [
            {"text": "I love discovering 'how things work'", "science": 4, "commerce": 0, "arts": 1, "vocational": 3},
            {"text": "I enjoy writing and creative expression", "science": 0, "commerce": 1, "arts": 4, "vocational": 0},
            {"text": "I'm interested in business and entrepreneurship", "science": 1, "commerce": 4, "arts": 1, "vocational": 1},
            {"text": "I prefer practical, immediate results", "science": 1, "commerce": 1, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 8,
        "question": "Your approach to a problem is to:",
        "options": [
            {"text": "Analyze data and use scientific method", "science": 4, "commerce": 2, "arts": 0, "vocational": 1},
            {"text": "Research and study different perspectives", "science": 0, "commerce": 1, "arts": 4, "vocational": 0},
            {"text": "Apply business logic and financial analysis", "science": 1, "commerce": 4, "arts": 1, "vocational": 0},
            {"text": "Find practical hands-on solutions", "science": 1, "commerce": 0, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 9,
        "question": "What's your ideal work environment?",
        "options": [
            {"text": "Laboratory, research center, or tech company", "science": 4, "commerce": 0, "arts": 0, "vocational": 1},
            {"text": "Media, publishing, or government office", "science": 0, "commerce": 1, "arts": 4, "vocational": 0},
            {"text": "Corporate office or trading floor", "science": 0, "commerce": 4, "arts": 1, "vocational": 0},
            {"text": "Workshop, factory, or field work", "science": 1, "commerce": 0, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 10,
        "question": "How important is continued education to you?",
        "options": [
            {"text": "Very important - love learning forever", "science": 4, "commerce": 2, "arts": 4, "vocational": 1},
            {"text": "Important - want specialized skills", "science": 2, "commerce": 3, "arts": 2, "vocational": 3},
            {"text": "Moderate - practical experience matters", "science": 1, "commerce": 2, "arts": 1, "vocational": 2},
            {"text": "Less important - learn on the job", "science": 0, "commerce": 1, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 11,
        "question": "Which achievement would satisfy you most?",
        "options": [
            {"text": "Inventing something or making a scientific discovery", "science": 4, "commerce": 0, "arts": 1, "vocational": 2},
            {"text": "Writing a book or creating impactful content", "science": 0, "commerce": 0, "arts": 4, "vocational": 0},
            {"text": "Building a successful business empire", "science": 0, "commerce": 4, "arts": 1, "vocational": 1},
            {"text": "Mastering a skilled trade perfectly", "science": 1, "commerce": 0, "arts": 0, "vocational": 4}
        ]
    },
    {
        "id": 12,
        "question": "What's your current academic strength?",
        "options": [
            {"text": "Science & Maths are my strong subjects", "science": 4, "commerce": 1, "arts": 0, "vocational": 2},
            {"text": "Language & Social Studies are my best", "science": 0, "commerce": 1, "arts": 4, "vocational": 0},
            {"text": "Good at Math and business subjects", "science": 2, "commerce": 4, "arts": 0, "vocational": 1},
            {"text": "All subjects equally or prefer practical work", "science": 1, "commerce": 1, "arts": 1, "vocational": 4}
        ]
    }
]

# Stream Information
STREAM_INFO = {
    "science": {
        "icon": "🔬",
        "title": "Science",
        "color": "#667eea",
        "description": "Study Physics, Chemistry, and Mathematics to explore careers in engineering, medicine, and research",
        "about": "Science stream is perfect for students interested in understanding the natural world through experimentation and analysis.",
        "why_choose": "If you enjoy problem-solving, hands-on experiments, and exploring how things work, Science is ideal for you.",
        "skills_needed": "Analytical thinking, mathematical ability, attention to detail, laboratory skills, and curiosity about nature",
        "degrees": [
            {"name": "B.Tech Engineering", "duration": "4 years", "salary": "₹8-15 LPA"},
            {"name": "MBBS Medicine", "duration": "5.5 years", "salary": "₹10-25 LPA"},
            {"name": "B.Sc Physics", "duration": "3 years", "salary": "₹5-12 LPA"},
            {"name": "B.Sc Chemistry", "duration": "3 years", "salary": "₹5-12 LPA"},
            {"name": "B.Pharmacy", "duration": "4 years", "salary": "₹6-15 LPA"}
        ],
        "careers": [
            {"title": "Software Engineer", "salary": "₹15-40 LPA"},
            {"title": "Civil Engineer", "salary": "₹8-20 LPA"},
            {"title": "Doctor/Physician", "salary": "₹15-50 LPA"},
            {"title": "Scientist", "salary": "₹8-18 LPA"},
            {"title": "Pharmacist", "salary": "₹6-15 LPA"},
            {"title": "Data Scientist", "salary": "₹12-30 LPA"}
        ],
        "exams": [
            {"name": "JEE Main/Advanced", "frequency": "Yearly"},
            {"name": "NEET", "frequency": "Yearly"},
            {"name": "BITSAT", "frequency": "Yearly"},
            {"name": "KVPY", "frequency": "Yearly"}
        ]
    },
    "commerce": {
        "icon": "📊",
        "title": "Commerce",
        "color": "#f39c12",
        "description": "Learn accounting, economics, and business management for careers in finance and entrepreneurship",
        "about": "Commerce stream develops skills in business, accounting, and financial management.",
        "why_choose": "Perfect if you're interested in business, finance, accounting, and managing enterprises.",
        "skills_needed": "Numerical ability, business acumen, analytical skills, communication, and financial literacy",
        "degrees": [
            {"name": "B.Com (Bachelor of Commerce)", "duration": "3 years", "salary": "₹6-12 LPA"},
            {"name": "B.B.A (Business Admin)", "duration": "3 years", "salary": "₹8-18 LPA"},
            {"name": "CA (Chartered Accountant)", "duration": "4.5 years", "salary": "₹10-30 LPA"},
            {"name": "CS (Company Secretary)", "duration": "4.5 years", "salary": "₹8-20 LPA"},
            {"name": "M.B.A", "duration": "2 years", "salary": "₹12-40 LPA"}
        ],
        "careers": [
            {"title": "Chartered Accountant", "salary": "₹15-50 LPA"},
            {"title": "Management Consultant", "salary": "₹12-30 LPA"},
            {"title": "Investment Banker", "salary": "₹20-60 LPA"},
            {"title": "Entrepreneur", "salary": "Variable"},
            {"title": "Financial Analyst", "salary": "₹10-25 LPA"},
            {"title": "Company Secretary", "salary": "₹10-25 LPA"}
        ],
        "exams": [
            {"name": "CA Foundation", "frequency": "Twice yearly"},
            {"name": "CS Foundation", "frequency": "Twice yearly"},
            {"name": "CAT (for MBA)", "frequency": "Yearly"},
            {"name": "IPCC", "frequency": "Twice yearly"}
        ]
    },
    "arts": {
        "icon": "📚",
        "title": "Arts",
        "color": "#e74c3c",
        "description": "Study humanities and social sciences for careers in law, journalism, and public service",
        "about": "Arts stream focuses on understanding society, culture, history, and human expression.",
        "why_choose": "Ideal if you're passionate about literature, history, social studies, or pursuing careers in law and journalism.",
        "skills_needed": "Strong communication, critical thinking, research ability, writing skills, and cultural awareness",
        "degrees": [
            {"name": "B.A (Bachelor of Arts)", "duration": "3 years", "salary": "₹5-10 LPA"},
            {"name": "LL.B (Law)", "duration": "3-5 years", "salary": "₹8-30 LPA"},
            {"name": "Journalism", "duration": "3 years", "salary": "₹6-15 LPA"},
            {"name": "Psychology", "duration": "3 years", "salary": "₹6-12 LPA"},
            {"name": "Political Science", "duration": "3 years", "salary": "₹6-12 LPA"}
        ],
        "careers": [
            {"title": "Lawyer", "salary": "₹10-50 LPA"},
            {"title": "Journalist", "salary": "₹8-20 LPA"},
            {"title": "IAS Officer", "salary": "₹56000-250000 monthly"},
            {"title": "Teacher", "salary": "₹6-15 LPA"},
            {"title": "Psychologist", "salary": "₹8-20 LPA"},
            {"title": "Content Writer", "salary": "₹6-15 LPA"}
        ],
        "exams": [
            {"name": "UPSC CSE", "frequency": "Yearly"},
            {"name": "CLAT", "frequency": "Yearly"},
            {"name": "JNUEE", "frequency": "Yearly"},
            {"name": "Delhi University Entrance", "frequency": "Yearly"}
        ]
    },
    "vocational": {
        "icon": "🔧",
        "title": "Vocational",
        "color": "#27ae60",
        "description": "Learn practical skills in trades and technology for immediate employment opportunities",
        "about": "Vocational training provides hands-on skills in specific trades and technical fields.",
        "why_choose": "Perfect if you prefer practical learning and want to enter the job market quickly with marketable skills.",
        "skills_needed": "Practical aptitude, technical understanding, problem-solving, hands-on learning, and communication",
        "degrees": [
            {"name": "ITI (Industrial Training)", "duration": "1-2 years", "salary": "₹4-8 LPA"},
            {"name": "Diploma in Engineering", "duration": "3 years", "salary": "₹6-12 LPA"},
            {"name": "Diploma in Nursing", "duration": "3 years", "salary": "₹5-10 LPA"},
            {"name": "Hotel Management", "duration": "3 years", "salary": "₹6-15 LPA"},
            {"name": "Automotive Technology", "duration": "2 years", "salary": "₹5-10 LPA"}
        ],
        "careers": [
            {"title": "Electrician", "salary": "₹5-12 LPA"},
            {"title": "Plumber", "salary": "₹4-10 LPA"},
            {"title": "Mechanic", "salary": "₹5-12 LPA"},
            {"title": "Chef", "salary": "₹6-15 LPA"},
            {"title": "Nurse", "salary": "₹5-12 LPA"},
            {"title": "Technician", "salary": "₹6-15 LPA"}
        ],
        "exams": [
            {"name": "ITI Entrance", "frequency": "Yearly"},
            {"name": "NCVT", "frequency": "Yearly"},
            {"name": "SCVT", "frequency": "Yearly"},
            {"name": "Vocational Board Exam", "frequency": "Yearly"}
        ]
    }
}

# Government Colleges
GOVERNMENT_COLLEGES = {
    "srinagar": [
        {
            "id": 1,
            "name": "University of Kashmir",
            "city": "Srinagar",
            "state": "Jammu & Kashmir",
            "established": 1948,
            "streams": ["Science", "Arts", "Commerce"],
            "cutoff": "70-80%",
            "facilities": ["Library", "Hostel", "Labs", "WiFi", "Sports", "Canteen", "Medical Center"],
            "contact": "+91-194-2272200",
            "email": "registrar@kashmiruniversity.ac.in",
            "website": "www.kashmiruniversity.ac.in",
            "description": "Central University offering undergraduate and postgraduate programs in Science, Arts, and Commerce streams."
        },
        {
            "id": 2,
            "name": "Sri Pratap College",
            "city": "Srinagar",
            "state": "Jammu & Kashmir",
            "established": 1821,
            "streams": ["Science", "Arts"],
            "cutoff": "65-75%",
            "facilities": ["Library", "Hostel", "Labs", "Canteen", "Gymnasium", "Auditorium"],
            "contact": "+91-194-2226541",
            "email": "admin@sripratap.edu.in",
            "website": "www.sripratap.edu.in",
            "description": "Historic institution with strong emphasis on Science and Arts education with modern research facilities."
        },
        {
            "id": 5,
            "name": "Amar Singh College",
            "city": "Srinagar",
            "state": "Jammu & Kashmir",
            "established": 1915,
            "streams": ["Science", "Arts", "Commerce"],
            "cutoff": "60-70%",
            "facilities": ["Library", "Labs", "Computer Center", "Cafeteria", "Sports Ground"],
            "contact": "+91-194-2470000",
            "email": "info@amarsinghcollege.ac.in",
            "website": "www.amarsinghcollege.ac.in",
            "description": "Premier college offering diverse academic programs with focus on student development."
        }
    ],
    "jammu": [
        {
            "id": 3,
            "name": "Jammu University",
            "city": "Jammu",
            "state": "Jammu & Kashmir",
            "established": 1969,
            "streams": ["Science", "Arts", "Commerce", "Vocational"],
            "cutoff": "60-75%",
            "facilities": ["Library", "Hostel", "Labs", "WiFi", "Cafeteria", "Sports Complex", "Auditorium"],
            "contact": "+91-191-2438080",
            "email": "registrar@jammuuniversity.ac.in",
            "website": "www.jammuuniversity.ac.in",
            "description": "Central University with comprehensive academic offerings and modern infrastructure across all streams."
        },
        {
            "id": 4,
            "name": "Government College for Women",
            "city": "Jammu",
            "state": "Jammu & Kashmir",
            "established": 1952,
            "streams": ["Science", "Arts", "Commerce"],
            "cutoff": "65-78%",
            "facilities": ["Library", "Hostel", "Labs", "WiFi", "Counseling Center", "Gymnasium"],
            "contact": "+91-191-2437800",
            "email": "gcwjammu@gmail.com",
            "website": "www.gcwjammu.edu.in",
            "description": "Exclusive institution for women with quality education and safe, supportive environment."
        },
        {
            "id": 6,
            "name": "Cluster University Samba",
            "city": "Jammu",
            "state": "Jammu & Kashmir",
            "established": 2007,
            "streams": ["Science", "Arts", "Commerce"],
            "cutoff": "55-65%",
            "facilities": ["Modern Labs", "Hostel", "WiFi", "Library", "Sports Facilities", "Cafeteria"],
            "contact": "+91-191-2558000",
            "email": "admin@cusamaba.ac.in",
            "website": "www.cusamaba.ac.in",
            "description": "Contemporary university with state-of-the-art facilities and innovative teaching methodologies."
        }
    ],
    "leh": [
        {
            "id": 7,
            "name": "Ladakh University",
            "city": "Leh",
            "state": "Jammu & Kashmir",
            "established": 2018,
            "streams": ["Science", "Arts", "Commerce"],
            "cutoff": "50-60%",
            "facilities": ["Library", "Hostel", "Labs", "WiFi", "Cafe", "Outdoor Sports"],
            "contact": "+91-194-2262005",
            "email": "registrar@ladakhuniversity.ac.in",
            "website": "www.ladakhuniversity.ac.in",
            "description": "New generation university providing quality higher education in beautiful Ladakh region."
        },
        {
            "id": 8,
            "name": "Leh Government College",
            "city": "Leh",
            "state": "Jammu & Kashmir",
            "established": 1974,
            "streams": ["Science", "Arts"],
            "cutoff": "45-55%",
            "facilities": ["Library", "Science Labs", "Hostel", "Cafeteria"],
            "contact": "+91-194-2262100",
            "email": "lehjk@college.edu.in",
            "website": "www.lehcollege.edu.in",
            "description": "Premier institution in Leh region with strong academic tradition and community engagement."
        }
    ],
    "anantnag": [
        {
            "id": 9,
            "name": "IUST (Islamic University of Science and Technology)",
            "city": "Anantnag",
            "state": "Jammu & Kashmir",
            "established": 2005,
            "streams": ["Science", "Commerce", "Vocational"],
            "cutoff": "65-75%",
            "facilities": ["Advanced Labs", "Hostel", "WiFi", "Library", "Research Center", "Cafeteria"],
            "contact": "+91-192-2232300",
            "email": "admissions@iust.ac.in",
            "website": "www.iust.ac.in",
            "description": "Renowned institution offering quality education in Science, Technology, and vocational training."
        }
    ],
    "kargil": [
        {
            "id": 10,
            "name": "Kargil College",
            "city": "Kargil",
            "state": "Jammu & Kashmir",
            "established": 1976,
            "streams": ["Arts", "Commerce"],
            "cutoff": "40-50%",
            "facilities": ["Library", "Classrooms", "Hostel", "Sports Ground"],
            "contact": "+91-194-5602300",
            "email": "kargil.college@edu.in",
            "website": "www.kargil.college.ac.in",
            "description": "Community college serving the Kargil region with focus on humanities and social sciences."
        }
    ]
}

# ============ DATABASE INITIALIZATION ============

def init_db():
    """Initialize database with ONE demo user"""
    with app.app_context():
        # Drop all tables and recreate them
        db.drop_all()
        db.create_all()
        
        # Create ONE demo user
        demo_user = User()
        demo_user.email = "demo@example.com"
        demo_user.name = "Demo Student"
        demo_user.class_level = "12"
        demo_user.stream = "Science"
        demo_user.phone = "9876543210"
        demo_user.state = "Jammu & Kashmir"
        demo_user.city = "Srinagar"
        demo_user.academic_percentage = 85
        demo_user.set_password("demo123")
        
        db.session.add(demo_user)
        db.session.commit()
        print("✅ Database initialized with ONE demo user: demo@example.com / demo123")

# Initialize database on startup
init_db()

# ============ ROUTES ============

@app.route("/")
def landing():
    """Landing page"""
    return render_template("landing.html", 
                         is_logged_in='user_id' in session,
                         user_name=session.get('user_name'))

@app.route("/login", methods=["GET", "POST"])
def login():
    """Login page with database backend"""
    if request.method == "POST":
        email = request.form.get("identifier", "").strip().lower()
        password = request.form.get("password", "")
        
        print(f"\n🔍 Login attempt: {email}")
        
        if not email or not password:
            error = "Please enter both email and password."
            demo_users = []
            return render_template("login.html", error=error, success=None, demo_users=demo_users)
        
        # Query database for user
        user = User.query.filter_by(email=email).first()
        print(f"   User found: {user is not None}")
        
        if user and user.check_password(password):
            # Set session with database user data
            session.permanent = True
            app.permanent_session_lifetime = timedelta(days=7)
            
            session['user_id'] = user.id
            session['user_name'] = user.name
            session['user_email'] = user.email
            session['user_class'] = user.class_level
            session['user_city'] = user.city
            session['user_state'] = user.state
            session['user_stream'] = user.stream
            session['user_percentage'] = user.academic_percentage
            
            session.modified = True
            
            print(f"✅ Login SUCCESS: {user.name} (ID: {user.id})")
            print(f"   Session data set: user_id={session.get('user_id')}")
            
            return redirect(url_for("dashboard"))
        else:
            error = "❌ Invalid email or password. Try: demo@example.com / demo123"
            print(f"❌ Login FAILED - Invalid credentials")
            demo_users = []
            return render_template("login.html", error=error, success=None, demo_users=demo_users)
    
    # GET request - show login page
    # Show demo user info
    demo_user = User.query.first()
    demo_users = []
    if demo_user:
        demo_users = [{"email": demo_user.email, "password": "demo123", "name": demo_user.name}]
    
    return render_template("login.html", error=None, success=None, demo_users=demo_users)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Sign up page with new user registration"""
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        name = request.form.get("name", "").strip()
        class_level = request.form.get("class_level", "").strip()
        phone = request.form.get("phone", "").strip()
        city = request.form.get("city", "").strip()
        state = request.form.get("state", "").strip()
        
        # Validation
        if not all([email, password, name, class_level, phone, city, state]):
            error = "All fields are required."
            return render_template("signup.html", error=error, success=None)
        
        if len(password) < 6:
            error = "Password must be at least 6 characters long."
            return render_template("signup.html", error=error, success=None)
        
        if User.query.filter_by(email=email).first():
            error = "Email already registered. Please login instead."
            return render_template("signup.html", error=error, success=None)
        
        try:
            # Create new user
            new_user = User()
            new_user.email = email
            new_user.name = name
            new_user.class_level = class_level
            new_user.phone = phone
            new_user.city = city
            new_user.state = state
            new_user.stream = "Not Selected"
            new_user.academic_percentage = 0
            new_user.set_password(password)
            
            db.session.add(new_user)
            db.session.commit()
            
            # Log in the new user immediately
            session.permanent = True
            app.permanent_session_lifetime = timedelta(days=7)
            session['user_id'] = new_user.id
            session['user_name'] = new_user.name
            session['user_email'] = new_user.email
            session['user_class'] = new_user.class_level
            session['user_city'] = new_user.city
            session['user_state'] = new_user.state
            session['user_stream'] = new_user.stream
            session['user_percentage'] = new_user.academic_percentage
            session.modified = True
            
            print(f"✅ New user registered and auto-logged in: {new_user.name}")
            return redirect(url_for("dashboard"))
        except Exception as e:
            error = f"Error creating account: {str(e)}"
            print(f"❌ Signup error: {error}")
            return render_template("signup.html", error=error, success=None)
    
    return render_template("signup.html", error=None, success=None)

@app.route("/dashboard")
def dashboard():
    """User dashboard - protected route"""
    if 'user_id' not in session:
        return redirect(url_for("login"))
    
    # Handle guest user (user_id = 0)
    if session['user_id'] == 0:
        user = {"id": 0, "name": "Guest User", "class_level": "N/A", "city": "N/A", "state": "N/A", "academic_percentage": "N/A", "email": "guest@example.com"}
        return render_template("dashboard.html", user=user, selected_college_name=session.get('selected_college'), quiz_stream=session.get('quiz_stream'), selected_college_id=session.get('selected_college_id'))
    
    user = db.session.get(User, session['user_id'])
    if not user:
        session.clear()
        return redirect(url_for("login"))
    
    # Get selected college info from session or user record
    selected_college = session.get('selected_college') or user.selected_college
    selected_college_id = session.get('selected_college_id') or user.selected_college_id
    
    print(f"✅ Dashboard loaded for: {user.name}")
    return render_template("dashboard.html", user=user, selected_college_name=selected_college, quiz_stream=session.get('quiz_stream'), selected_college_id=selected_college_id)

@app.route("/quiz")
def quiz():
    """Quiz page - protected route"""
    # Check if user is logged in
    if 'user_id' not in session:
        print("⚠️  Quiz: No user_id in session, redirecting to login")
        return redirect(url_for("login"))
    
    try:
        # Get user data for personalized quiz
        user_id = session.get('user_id')
        print(f"🎯 Quiz: Loading for user_id={user_id}")
        
        user = User.query.get(user_id)
        if not user:
            print(f"❌ Quiz: User {user_id} not found in database")
            session.clear()
            return redirect(url_for("login"))
        
        # Safe data extraction with defaults
        user_data = {
            'name': user.name or 'Student',
            'class_level': user.class_level or 'Not Selected',
            'academic_percentage': user.academic_percentage or 0,
            'stream': user.stream or 'Not Selected',
            'city': getattr(user, 'city', None) or 'Not Selected',
            'subject_level': 'advanced' if (user.academic_percentage and user.academic_percentage >= 75) else 'intermediate' if (user.academic_percentage and user.academic_percentage >= 50) else 'basic'
        }
        
        print(f"✅ Quiz: User data loaded: {user_data['name']}")
        return render_template("quiz.html", user_data=user_data)
    
    except Exception as e:
        print(f"❌ Quiz Error: {str(e)}")
        return redirect(url_for("login"))

@app.route("/api/save-quiz-result", methods=["POST"])
def save_quiz_result():
    """Save quiz result to database"""
    if 'user_id' not in session:
        return jsonify({"error": "Not authenticated"}), 401
    
    data = request.get_json()
    user_id = session['user_id']
    
    # Create quiz result record
    quiz_result = QuizResult()
    quiz_result.user_id = user_id
    quiz_result.science_score = data.get('science', 0)
    quiz_result.commerce_score = data.get('commerce', 0)
    quiz_result.arts_score = data.get('arts', 0)
    quiz_result.vocational_score = data.get('vocational', 0)
    quiz_result.recommended_stream = data.get('stream', 'science')
    
    db.session.add(quiz_result)
    db.session.commit()
    
    print(f"✅ Quiz result saved for user {user_id}: {quiz_result.recommended_stream}")
    return jsonify({"success": True, "result_id": quiz_result.id})

@app.route("/api/colleges", methods=["GET"])
def api_colleges():
    """API endpoint to return all colleges in JSON format"""
    try:
        colleges_json_path = os.path.join(os.path.dirname(__file__), 'data', 'colleges_data.json')
        with open(colleges_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Transform colleges data to match frontend expectations
        colleges = []
        for idx, college in enumerate(data['colleges'], 1):
            transformed = {
                'id': idx,
                'name': college.get('name', ''),
                'city': college.get('city', ''),
                'state': college.get('state', ''),
                'stream': college.get('college_type', ''),  # Use college_type as stream
                'degree': college.get('degree_type', 'B.Tech'),
                'fees': str(college.get('total_fees', 0) / 100000),  # Convert to lakhs
                'rating': 4.0 + (idx % 5) * 0.2,  # Generate rating based on index
                'admissionType': college.get('admission_type', ''),
                'programs': college.get('branches', []),
                'established': college.get('established_year', 2000),
                'facilities': college.get('facilities', []),
                'description': college.get('description', ''),
                'placement': f"{80 + (idx % 20)}%",  # Generate placement percentage
                'avgPackage': f"{4 + (idx % 8)} LPA",  # Generate avg package
                'cutoff': college.get('cutoff_percentage', 50),
                'website': college.get('website', ''),
                'contact': college.get('contact_phone', ''),
                'email': college.get('contact_email', '')
            }
            colleges.append(transformed)
        
        return jsonify({'colleges': colleges})
    except Exception as e:
        print(f"Error loading colleges: {e}")
        return jsonify({'error': str(e)}), 500

@app.route("/result")
def result():
    """Results page with personalized recommendations"""
    if 'user_id' not in session:
        return redirect(url_for("login"))
    
    # Get user data
    user = User.query.get(session['user_id'])
    if not user:
        session.clear()
        return redirect(url_for("login"))
    
    # Get stream and scores from query params
    stream = request.args.get("stream", "science").lower()
    overall_score = int(request.args.get('overall_score', 85))
    match_score = int(request.args.get('match_score', 88))
    
    # Get scores from query params
    scores = {
        'science': int(request.args.get('science', 65)),
        'commerce': int(request.args.get('commerce', 45)),
        'arts': int(request.args.get('arts', 40)),
        'vocational': int(request.args.get('vocational', 35))
    }
    
    # Validate stream
    if stream not in STREAM_INFO:
        stream = "science"
    
    # Determine difficulty level
    if user.academic_percentage and user.academic_percentage >= 75:
        difficulty_level = 'advanced'
        difficulty_description = 'Advanced difficulty assessment'
    elif user.academic_percentage and user.academic_percentage >= 50:
        difficulty_level = 'intermediate'
        difficulty_description = 'Intermediate difficulty assessment'
    else:
        difficulty_level = 'basic'
        difficulty_description = 'Basic difficulty assessment'
    
    # Prepare user data for template
    user_data = {
        'name': user.name if user.name else 'Student',
        'class_level': user.class_level if user.class_level else 'Not Selected',
        'academic_percentage': user.academic_percentage if user.academic_percentage else 0,
        'stream': user.stream if user.stream else 'Not Selected',
        'city': user.city if hasattr(user, 'city') and user.city else 'Not Selected'
    }
    
    stream_info = STREAM_INFO[stream]
    
    # Store stream in session for later use
    session['quiz_stream'] = stream
    session['quiz_scores'] = scores
    session.modified = True
    
    return render_template(
        "result.html",
        stream_info=stream_info,
        scores=scores,
        user_data=user_data,
        overall_score=overall_score,
        match_score=match_score,
        difficulty_level=difficulty_level,
        difficulty_description=difficulty_description,
        stream=stream
    )

@app.route("/colleges")
def colleges():
    """Colleges directory"""
    city = request.args.get("city", "").lower()
    stream_param = request.args.get("stream") or session.get('quiz_stream', "")
    stream = stream_param.lower() if stream_param else ""
    course_type = request.args.get("course_type", "").lower()
    
    # Load colleges from JSON file
    colleges_json_path = os.path.join(os.path.dirname(__file__), 'data', 'colleges_data.json')
    with open(colleges_json_path, 'r', encoding='utf-8') as f:
        colleges_data = json.load(f)
    
    colleges_list = colleges_data['colleges']
    
    # Apply filters
    if city:
        colleges_list = [c for c in colleges_list if c.get('city', '').lower() == city]
    
    if stream:
        colleges_list = [c for c in colleges_list if stream in [s.lower() for s in c.get('streams', [])]]
    
    if course_type:
        colleges_list = [c for c in colleges_list if c.get('college_type', '').lower() == course_type]
    
    # Get all unique cities for dropdown
    all_cities = sorted(list(set([c.get('city', '') for c in colleges_data['colleges']])))
    
    # Get authentication info
    is_logged_in = 'user_id' in session
    user_name = session.get('user_name', '')
    
    return render_template("colleges.html", colleges=colleges_list, city=city, stream=stream, all_cities=all_cities, is_logged_in=is_logged_in, user_name=user_name)

@app.route("/set_selected_college", methods=['POST'])
def set_selected_college():
    """Store the selected college in user session and database"""
    if 'user_id' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    
    try:
        data = request.get_json()
        college_id = data.get('college_id')
        college_name = data.get('college_name')
        
        # Update session
        session['selected_college'] = college_name
        session['selected_college_id'] = college_id
        session.modified = True
        
        # Update database if user is logged in
        user = User.query.get(session['user_id'])
        if user:
            user.selected_college = college_name
            user.selected_college_id = college_id
            db.session.commit()
        
        return jsonify({'success': True, 'message': f'{college_name} selected!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/career-paths")
def career_paths():
    """Career paths page with detailed career information"""
    is_logged_in = 'user_id' in session
    user_name = session.get('user_name', '')
    
    # Get stream from query or session
    stream = (request.args.get("stream") or session.get('quiz_stream', "")).lower()
    
    # Get user's quiz result if they are logged in
    user_stream = stream  # Use the stream from query/session
    if not user_stream and is_logged_in:
        user = User.query.get(session.get('user_id'))
        if user:
            quiz_result = QuizResult.query.filter_by(user_id=user.id).order_by(QuizResult.completed_at.desc()).first()
            if quiz_result:
                user_stream = quiz_result.recommended_stream.lower()
    
    return render_template("career_paths.html", is_logged_in=is_logged_in, user_name=user_name, user_stream=user_stream, stream=user_stream)

@app.route("/about")
def about():
    """About page"""
    is_logged_in = 'user_id' in session
    user_name = session.get('user_name', '')
    return render_template("about.html", is_logged_in=is_logged_in, user_name=user_name)

@app.route("/logout")
def logout():
    """Logout"""
    session.clear()
    return redirect(url_for("landing"))

@app.route("/guest")
def guest():
    """Guest mode - access without login"""
    session['user_id'] = 0  # 0 = guest
    session['user_name'] = "Guest User"
    session['user_email'] = "guest@example.com"
    session['user_class'] = "N/A"
    session['user_city'] = "N/A"
    session['user_state'] = "N/A"
    session['user_stream'] = "Not Selected"
    session['user_percentage'] = 0
    session.permanent = True
    session.modified = True
    
    print("✅ Guest session started")
    return redirect(url_for("dashboard"))

@app.errorhandler(404)
def not_found(error):
    """404 handler"""
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(error):
    """500 handler"""
    return render_template("500.html"), 500

@app.context_processor
def inject_user():
    """Make user info available in templates"""
    return dict(
        user_name=session.get('user_name'),
        is_logged_in='user_id' in session
    )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, host="127.0.0.1", port=5000)
