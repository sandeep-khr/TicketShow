from functools import wraps
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    is_admin = data.get('is_admin', False)  # New field for admin registration

    if not username or not password or not email:
        return jsonify(error='Missing username or password or email'), 400

    user = User.query.filter_by(username=username).first()

    if user:
        return jsonify(error='Username already exists'), 409

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, is_admin=is_admin, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message='Signup successful'), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify(error='Missing username or password'), 400

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify(error='Invalid username or password'), 401

    access_token = create_access_token(identity={'id': user.id, 'username': user.username, 'is_admin': user.is_admin})

    return jsonify(access_token=access_token)


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        if not current_user['is_admin']:
            return jsonify(error='Admin access required'), 403
        return fn(*args, **kwargs)

    return wrapper

@auth_bp.route('/add_admin', methods=['POST'])
@admin_required
def add_admin():
    data = request.json
    username = data.get('username')
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify(error='User not found'), 404
    user.is_admin = True    
    db.session.commit()
    return jsonify(message='Admin added successfully'), 201
