from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/user/profile', methods=['GET'])
@jwt_required()
def get_user_profile():
    current_user = User.query.get(get_jwt_identity()['id'])
    if not current_user:
        return jsonify(error='User not found'), 404

    user_profile = {
        'id': current_user.id,
        'username': current_user.username,
        'is_admin': current_user.is_admin
    }

    return jsonify(user_profile)

@user_bp.route('/user/bookings', methods=['GET'])
@jwt_required()
def get_user_bookings():
    current_user = User.query.get(get_jwt_identity()['id'])
    if not current_user:
        return jsonify(error='User not found'), 404

    bookings = current_user.bookings
    bookings_data = []

    for booking in bookings:
        booking_data = {
            'id': booking.id,
            'show_id': booking.show_id,
            'quantity': booking.quantity,
            'booking_date': booking.booking_date.strftime('%Y-%m-%d %H:%M:%S')
        }
        bookings_data.append(booking_data)

    return jsonify(bookings_data)
