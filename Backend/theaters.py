from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models import db, Theatre
from auth import admin_required
from workers import cache

theater_bp = Blueprint('theater', __name__)

@theater_bp.route('/theater', methods=['GET'])
@cache.cached(timeout=10, key_prefix='all_theaters')
def get_theaters():
    theaters = Theatre.query.all()
    theaters_data = []

    for theater in theaters:
        theater_data = {
            'id': theater.id,
            'name': theater.name,
            'place': theater.place,
            'capacity': theater.capacity,
            'shows': [show.id for show in theater.shows]
        }
        theaters_data.append(theater_data)

    return jsonify(theaters_data)

@theater_bp.route('/theater/<int:theater_id>', methods=['GET'])
@cache.memoize(10)
def get_theater(theater_id):
    theater = Theatre.query.get(theater_id)

    if not theater:
        return jsonify(error = 'Theater Not Found'), 404
    
    theater_data = {
        'id': theater.id,
        'name': theater.name,
        'place': theater.place,
        'capacity': theater.capacity,
        'shows': [show.id for show in theater.shows]
    }
    return jsonify(theater_data)


@theater_bp.route('/theater', methods=['POST'])
@jwt_required()
@admin_required
def create_theater():
    data = request.json
    name = data.get('name')
    place = data.get('place')
    capacity = data.get('capacity')

    if not name or not place or not capacity:
        return jsonify(error='Missing required fields'), 400

    theater = Theatre(name=name, place=place, capacity=capacity)
    db.session.add(theater)
    db.session.commit()

    # cache.delete('all_theaters') # delete the cache for the get_theaters function

    return jsonify(message='Theater created successfully'), 201


@theater_bp.route('/theater/<int:theater_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_theater(theater_id):
    theater = Theatre.query.get(theater_id)

    if not theater:
        return jsonify(error='Theater not found'), 404

    data = request.json
    name = data.get('name')
    place = data.get('place')
    capacity = data.get('capacity')

    if name:
        theater.name = name
    if place:
        theater.place = place
    if capacity:
        theater.capacity = capacity

    db.session.commit()

    # cache.delete_memoized(get_theater, theater_id) # delete the cache for the get_theater function

    return jsonify(message='Theater updated successfully')


@theater_bp.route('/theater/<int:theater_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_theater(theater_id):
    theater = Theatre.query.get(theater_id)

    if not theater:
        return jsonify(error='Theater not found'), 404

    db.session.delete(theater)
    db.session.commit()
    # cache.delete('all_theaters')

    return jsonify(message='Theater deleted successfully')



