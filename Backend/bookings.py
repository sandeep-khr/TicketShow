from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from models import db, Booking, Show, User, Theatre
from workers import cache

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/booking', methods=['GET'])
@jwt_required()
@cache.cached(timeout=10, key_prefix='all_bookings')
def get_bookings():
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
            'booking_date': booking.booking_date.strftime('%Y-%m-%d %H:%M:%S'),
            'amount': booking.amount,
            'movie_name': booking.movie_name
        }
        bookings_data.append(booking_data)

    return jsonify(bookings_data)

@booking_bp.route('/booking', methods=['POST'])
@jwt_required()
def create_booking():
    data = request.json
    show_id = data.get('show_id')
    quantity = data.get('quantity')

    if not show_id or not quantity:
        return jsonify(error='Missing show ID or quantity'), 400

    show = Show.query.get(show_id)
    if not show:
        return jsonify(error='Show not found'), 404

    current_user = User.query.get(get_jwt_identity()['id'])
    if not current_user:
        return jsonify(error='User not found'), 404

    if quantity > show.theatre.capacity:
        return jsonify(error='Not enough seats available'), 400

    amount = quantity * show.ticket_price
    movie_name = show.name
    booking = Booking(user_id=current_user.id, show_id=show.id, quantity=quantity, booking_date=datetime.now(), amount=amount, movie_name=movie_name)
    db.session.add(booking)
    
    show.theatre.capacity -= quantity

    db.session.commit()

    cache.delete('all_bookings')

    return jsonify(message='Booking created successfully'), 201

