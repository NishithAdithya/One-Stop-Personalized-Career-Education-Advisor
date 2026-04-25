"""
Database models for the Career Advisor Platform
Defines College, Program, Career, Exam, and related models
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class College(db.Model):
    """College model for storing college information"""
    
    __tablename__ = 'colleges'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True, index=True)
    college_type = db.Column(db.String(50))  # Engineering, Arts, BCA, Law, Pharmacy, B.Ed
    city = db.Column(db.String(50), nullable=False, index=True)
    state = db.Column(db.String(50), default='Jammu & Kashmir')
    established_year = db.Column(db.Integer)
    affiliation = db.Column(db.String(150))
    streams = db.Column(db.JSON)  # ['Science', 'Arts', 'Commerce']
    degree_type = db.Column(db.String(50), index=True)  # B.Tech, B.A., BCA, etc.
    duration_years = db.Column(db.Integer)
    total_fees = db.Column(db.Integer)  # In rupees
    annual_fees = db.Column(db.Integer)  # If applicable
    admission_type = db.Column(db.String(100))  # JEE Main, JEE Advanced, Merit, etc.
    cutoff_percentage = db.Column(db.Float)
    branches = db.Column(db.JSON)  # List of branches/programs
    subjects = db.Column(db.JSON)  # For arts colleges
    facilities = db.Column(db.JSON)  # Hostel, Library, Labs, WiFi, Sports
    contact_phone = db.Column(db.String(20))
    contact_email = db.Column(db.String(120))
    website = db.Column(db.String(200))
    description = db.Column(db.Text)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    rating = db.Column(db.Float, default=0.0)
    review_count = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    programs = db.relationship('Program', backref='college', lazy=True, cascade='all, delete-orphan')
    reviews = db.relationship('Review', backref='college', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        """Convert college to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'college_type': self.college_type,
            'city': self.city,
            'state': self.state,
            'established_year': self.established_year,
            'affiliation': self.affiliation,
            'streams': self.streams,
            'degree_type': self.degree_type,
            'duration_years': self.duration_years,
            'total_fees': self.total_fees,
            'annual_fees': self.annual_fees,
            'admission_type': self.admission_type,
            'cutoff_percentage': self.cutoff_percentage,
            'branches': self.branches,
            'subjects': self.subjects,
            'facilities': self.facilities,
            'contact_phone': self.contact_phone,
            'contact_email': self.contact_email,
            'website': self.website,
            'description': self.description,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'rating': self.rating,
            'review_count': self.review_count,
            'created_at': self.created_at.isoformat()
        }
    
    def __repr__(self):
        return f'<College {self.name}>'


class Program(db.Model):
    """Program/Degree model"""
    
    __tablename__ = 'programs'
    
    id = db.Column(db.Integer, primary_key=True)
    college_id = db.Column(db.Integer, db.ForeignKey('colleges.id'), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    degree_type = db.Column(db.String(50), nullable=False, index=True)
    stream = db.Column(db.String(50), index=True)
    duration_years = db.Column(db.Integer)
    description = db.Column(db.Text)
    salary_range = db.Column(db.String(50))
    career_options = db.Column(db.JSON)
    required_exams = db.Column(db.JSON)
    cutoff = db.Column(db.Float)
    intake = db.Column(db.Integer)  # Number of seats
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert program to dictionary"""
        return {
            'id': self.id,
            'college_id': self.college_id,
            'college_name': self.college.name if self.college else None,
            'name': self.name,
            'degree_type': self.degree_type,
            'stream': self.stream,
            'duration_years': self.duration_years,
            'description': self.description,
            'salary_range': self.salary_range,
            'career_options': self.career_options,
            'required_exams': self.required_exams,
            'cutoff': self.cutoff,
            'intake': self.intake
        }
    
    def __repr__(self):
        return f'<Program {self.name}>'


class Career(db.Model):
    """Career model for career information"""
    
    __tablename__ = 'careers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True, index=True)
    stream = db.Column(db.String(50), index=True)
    avg_salary = db.Column(db.Integer)
    description = db.Column(db.Text)
    required_skills = db.Column(db.JSON)
    job_sectors = db.Column(db.JSON)
    growth_rate = db.Column(db.String(20))
    education_required = db.Column(db.String(100))
    companies = db.Column(db.JSON)
    job_roles = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert career to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'stream': self.stream,
            'avg_salary': self.avg_salary,
            'description': self.description,
            'required_skills': self.required_skills,
            'job_sectors': self.job_sectors,
            'growth_rate': self.growth_rate,
            'education_required': self.education_required,
            'companies': self.companies,
            'job_roles': self.job_roles
        }
    
    def __repr__(self):
        return f'<Career {self.name}>'


class EntranceExam(db.Model):
    """Entrance exam model"""
    
    __tablename__ = 'entrance_exams'
    
    id = db.Column(db.Integer, primary_key=True)
    exam_name = db.Column(db.String(150), nullable=False, unique=True, index=True)
    stream = db.Column(db.String(50), index=True)
    exam_type = db.Column(db.String(50))  # National, State, University
    description = db.Column(db.Text)
    eligibility = db.Column(db.String(200))
    exam_duration = db.Column(db.String(20))
    total_marks = db.Column(db.Integer)
    exam_fee = db.Column(db.Integer)
    application_deadline = db.Column(db.DateTime)
    exam_date = db.Column(db.DateTime)
    result_date = db.Column(db.DateTime)
    official_website = db.Column(db.String(200))
    syllabus = db.Column(db.Text)
    colleges_accepting = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert exam to dictionary"""
        return {
            'id': self.id,
            'exam_name': self.exam_name,
            'stream': self.stream,
            'exam_type': self.exam_type,
            'description': self.description,
            'eligibility': self.eligibility,
            'exam_duration': self.exam_duration,
            'total_marks': self.total_marks,
            'exam_fee': self.exam_fee,
            'application_deadline': self.application_deadline,
            'exam_date': self.exam_date,
            'result_date': self.result_date,
            'official_website': self.official_website,
            'colleges_accepting': self.colleges_accepting
        }
    
    def __repr__(self):
        return f'<EntranceExam {self.exam_name}>'


class UserPreferences(db.Model):
    """User preferences model"""
    
    __tablename__ = 'user_preferences'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, index=True)
    preferred_streams = db.Column(db.JSON)  # ['Science', 'Engineering']
    preferred_degrees = db.Column(db.JSON)  # ['B.Tech', 'B.Sc.']
    preferred_cities = db.Column(db.JSON)  # ['Jammu', 'Srinagar']
    budget_min = db.Column(db.Integer)
    budget_max = db.Column(db.Integer)
    saved_colleges = db.Column(db.JSON, default=[])
    saved_careers = db.Column(db.JSON, default=[])
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        """Convert preferences to dictionary"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'preferred_streams': self.preferred_streams,
            'preferred_degrees': self.preferred_degrees,
            'preferred_cities': self.preferred_cities,
            'budget_min': self.budget_min,
            'budget_max': self.budget_max,
            'saved_colleges': self.saved_colleges,
            'saved_careers': self.saved_careers
        }
    
    def __repr__(self):
        return f'<UserPreferences {self.user_id}>'


class Review(db.Model):
    """College review model"""
    
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    college_id = db.Column(db.Integer, db.ForeignKey('colleges.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    user_name = db.Column(db.String(100), default='Anonymous')
    rating = db.Column(db.Float, nullable=False)  # 1-5 stars
    title = db.Column(db.String(150))
    review_text = db.Column(db.Text)
    helpful_count = db.Column(db.Integer, default=0)
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        """Convert review to dictionary"""
        return {
            'id': self.id,
            'college_id': self.college_id,
            'user_id': self.user_id,
            'user_name': self.user_name,
            'rating': self.rating,
            'title': self.title,
            'review_text': self.review_text,
            'helpful_count': self.helpful_count,
            'is_verified': self.is_verified,
            'created_at': self.created_at.isoformat()
        }
    
    def __repr__(self):
        return f'<Review {self.id}>'


class Comparison(db.Model):
    """Temporary comparison storage"""
    
    __tablename__ = 'comparisons'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, index=True)
    college_ids = db.Column(db.JSON)  # List of college IDs
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime)  # For cleanup
    
    def to_dict(self):
        """Convert comparison to dictionary"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'college_ids': self.college_ids,
            'created_at': self.created_at.isoformat()
        }
    
    def __repr__(self):
        return f'<Comparison {self.id}>'


class StreamMapping(db.Model):
    """Stream to resources mapping"""
    
    __tablename__ = 'stream_mapping'
    
    id = db.Column(db.Integer, primary_key=True)
    stream = db.Column(db.String(50), unique=True, nullable=False, index=True)
    degrees = db.Column(db.JSON)  # List of degree types
    colleges = db.Column(db.JSON)  # List of college IDs
    careers = db.Column(db.JSON)  # List of career IDs
    exams = db.Column(db.JSON)  # List of exam IDs
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'stream': self.stream,
            'degrees': self.degrees,
            'colleges': self.colleges,
            'careers': self.careers,
            'exams': self.exams,
            'description': self.description
        }
    
    def __repr__(self):
        return f'<StreamMapping {self.stream}>'
