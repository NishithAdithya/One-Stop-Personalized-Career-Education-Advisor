"""
College routes/API endpoints
Handles all college-related requests
"""

from flask import Blueprint, request, jsonify
from models import db, College
from sqlalchemy import and_

colleges_bp = Blueprint('colleges', __name__, url_prefix='/api/colleges')


@colleges_bp.route('', methods=['GET'])
def get_colleges():
    """Get all colleges with optional filtering and pagination"""
    
    try:
        # Get query parameters
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 10, type=int)
        city = request.args.get('city', None)
        stream = request.args.get('stream', None)
        degree = request.args.get('degree', None)
        college_type = request.args.get('type', None)
        sort_by = request.args.get('sort', 'name', type=str)
        
        # Build query
        query = College.query
        
        # Apply filters
        if city:
            query = query.filter_by(city=city)
        if degree:
            query = query.filter_by(degree_type=degree)
        if college_type:
            query = query.filter_by(college_type=college_type)
        if stream:
            # Stream filter (any college that offers this stream)
            query = query.filter(College.streams.contains([stream]))
        
        # Apply sorting
        if sort_by == 'rating':
            query = query.order_by(College.rating.desc())
        elif sort_by == 'fees':
            query = query.order_by(College.total_fees.asc())
        else:
            query = query.order_by(College.name.asc())
        
        # Pagination
        paginated = query.paginate(page=page, per_page=limit, error_out=False)
        
        colleges = [college.to_dict() for college in paginated.items]
        
        return jsonify({
            'success': True,
            'total': paginated.total,
            'pages': paginated.pages,
            'current_page': page,
            'per_page': limit,
            'colleges': colleges
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@colleges_bp.route('/<int:college_id>', methods=['GET'])
def get_college(college_id):
    """Get single college details"""
    
    try:
        college = College.query.get_or_404(college_id)
        return jsonify({
            'success': True,
            'college': college.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 404


@colleges_bp.route('/search', methods=['GET'])
def search_colleges():
    """Search colleges by name or city"""
    
    try:
        query = request.args.get('q', '', type=str).lower()
        limit = request.args.get('limit', 10, type=int)
        
        if not query or len(query) < 2:
            return jsonify({
                'success': False,
                'error': 'Search query must be at least 2 characters'
            }), 400
        
        colleges = College.query.filter(
            (College.name.ilike(f'%{query}%')) |
            (College.city.ilike(f'%{query}%'))
        ).limit(limit).all()
        
        return jsonify({
            'success': True,
            'results': [college.to_dict() for college in colleges]
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@colleges_bp.route('/by-city/<city>', methods=['GET'])
def get_colleges_by_city(city):
    """Get colleges in a specific city"""
    
    try:
        colleges = College.query.filter_by(city=city).all()
        
        return jsonify({
            'success': True,
            'city': city,
            'total': len(colleges),
            'colleges': [college.to_dict() for college in colleges]
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@colleges_bp.route('/by-stream/<stream>', methods=['GET'])
def get_colleges_by_stream(stream):
    """Get colleges offering a specific stream"""
    
    try:
        colleges = College.query.filter(
            College.streams.contains([stream])
        ).all()
        
        return jsonify({
            'success': True,
            'stream': stream,
            'total': len(colleges),
            'colleges': [college.to_dict() for college in colleges]
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@colleges_bp.route('/by-degree/<degree>', methods=['GET'])
def get_colleges_by_degree(degree):
    """Get colleges offering a specific degree"""
    
    try:
        colleges = College.query.filter_by(degree_type=degree).all()
        
        return jsonify({
            'success': True,
            'degree': degree,
            'total': len(colleges),
            'colleges': [college.to_dict() for college in colleges]
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@colleges_bp.route('/filter', methods=['POST'])
def filter_colleges():
    """Advanced college filtering with multiple criteria"""
    
    try:
        filters = request.get_json() or {}
        
        query = College.query
        
        # Apply filters
        if 'cities' in filters and filters['cities']:
            query = query.filter(College.city.in_(filters['cities']))
        
        if 'streams' in filters and filters['streams']:
            for stream in filters['streams']:
                query = query.filter(College.streams.contains([stream]))
        
        if 'degree_types' in filters and filters['degree_types']:
            query = query.filter(College.degree_type.in_(filters['degree_types']))
        
        if 'college_types' in filters and filters['college_types']:
            query = query.filter(College.college_type.in_(filters['college_types']))
        
        if 'max_fees' in filters and filters['max_fees']:
            query = query.filter(College.total_fees <= filters['max_fees'])
        
        if 'min_fees' in filters and filters['min_fees']:
            query = query.filter(College.total_fees >= filters['min_fees'])
        
        colleges = query.all()
        
        return jsonify({
            'success': True,
            'total': len(colleges),
            'applied_filters': filters,
            'colleges': [college.to_dict() for college in colleges]
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@colleges_bp.route('/stats', methods=['GET'])
def get_college_stats():
    """Get statistics about colleges"""
    
    try:
        total_colleges = College.query.count()
        cities = db.session.query(College.city).distinct().count()
        streams = {}
        types = {}
        
        for college in College.query.all():
            if college.college_type:
                types[college.college_type] = types.get(college.college_type, 0) + 1
            if college.streams:
                for stream in college.streams:
                    streams[stream] = streams.get(stream, 0) + 1
        
        return jsonify({
            'success': True,
            'total_colleges': total_colleges,
            'total_cities': cities,
            'by_type': types,
            'by_stream': streams
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
