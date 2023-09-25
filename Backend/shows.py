from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Show, Theatre, UserVote, User, Booking, UserComment
from auth import admin_required
import os, requests, re
from datetime import datetime
from workers import cache

show_bp = Blueprint('show', __name__)

@show_bp.route('/show', methods=['GET'])
@cache.cached(timeout=10, key_prefix='all_shows')
def get_shows():
    shows = Show.query.all()
    shows_data = []

    for show in shows:
        show_data = {
            'id': show.id,
            'name': show.name,
            'rating': show.rating,
            'total_rating': show.num_votes,
            'tags': show.tags,
            'language': show.language,
            'show_date': show.show_date.strftime('%Y-%m-%d %H:%M:%S'),
            'movie_description': show.movie_description,
            'director': show.director,
            'writer':show.writer,
            'movie_length': show.movie_length,
            'image_url': show.image_url,
            'cast': show.cast,
            'youtube': show.youtube,
            'ticket_price': show.ticket_price,
            'location': show.location,
            'theatre_id': show.theatre_id,
            
            # 'votes': [{'user_id': vote.user_id, 'rating': vote.rating} for vote in show.votes],
            # 'bookings': [{'user_id': booking.user_id, 'quantity': booking.quantity, 'amount': booking.amount} for booking in show.bookings]
        }
        shows_data.append(show_data)
    return jsonify(shows_data)

@show_bp.route('/show/<int:show_id>', methods=['GET'])
@cache.memoize(10)
def get_show(show_id):
    show = Show.query.get(show_id)
    
    if not show:
        return jsonify(error = 'Show Not Found'), 404
    
    show_data = {
        'id': show.id,
        'name': show.name,
        'rating': show.rating,
        'total_rating': show.num_votes,
        'tags': show.tags,
        'language': show.language,
        'show_date': show.show_date.strftime('%Y-%m-%d %H:%M'),
        'movie_description': show.movie_description,
        'director': show.director,
        'writer':show.writer,
        'movie_length': show.movie_length,
        'image_url': show.image_url,
        'cast': show.cast,
        'youtube': show.youtube,
        'ticket_price': show.ticket_price,
        'location': show.location,
        'theatre_id': show.theatre_id,
        # 'comments': show.comments,
        # 'votes': show.votes,
        'comments_data': [
            {
                'user_id': comment.user_id,
                'c_username': comment.c_username,
                'comment': comment.comment,
                'commented_at': comment.commented_at.strftime('%Y-%m-%d %H:%M:%S')
            }
            for comment in show.comments
        ],
    }

    return jsonify(show_data)

@show_bp.route('/show', methods=['POST'])
@jwt_required()
@admin_required
def create_show():
    data = request.json
    name = data.get('name')
    rating = data.get('rating')
    tags = data.get('tags')
    language = data.get('language')
    ticket_price = data.get('ticket_price')
    date = data.get('date')
    theatre_id = data.get('theatre_id')
    youtube_url = data.get('youtube_url')

    # date_string = data['date']
    # date_format = '%Y-%m-%d %H:%M'
    # show_date = datetime.strptime(date, date_format)

    if not name or not tags or not language or not ticket_price or not theatre_id or not date or not youtube_url:
        return jsonify(error='Missing required fields'), 400

    theatre = Theatre.query.get(theatre_id)
    if not theatre:
        return jsonify(error='Theatre not found'), 404

    # Retrieve movie information from the OMDB API
    omdb_api_key = os.environ.get("OMDB_API_KEY")
    movie_title = name
    omdb_url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&t={movie_title}"
    response = requests.get(omdb_url)
    movie_data = response.json()

    if(movie_data.get('Response') == 'False'):
        return jsonify(error='Movie not found'), 404

    # Extract movie information
    movie_description = movie_data.get('Plot')
    director = movie_data.get('Director')
    movie_length = movie_data.get('Runtime')
    image_url = movie_data.get('Poster')
    cast = movie_data.get('Actors')
    writer=movie_data.get('Writer')

    url = youtube_url
    video_id = re.search(r"youtu\.be\/(.+)", url)
    if video_id:
        video_id = video_id.group(1)
    else:
        return jsonify(error='Video id not found'), 404

    timing_str = date
    show_date = datetime.strptime(timing_str, '%Y-%m-%dT%H:%M')

    show = Show(name=name, rating=rating, tags=tags, language=language, ticket_price=ticket_price,
                theatre_id=theatre.id, movie_description=movie_description, director=director, writer=writer,
                movie_length=movie_length, image_url=image_url, cast=cast, youtube=video_id, show_date=show_date)

    show.location = theatre.place

    db.session.add(show)
    db.session.commit()

    # cache.delete('all_shows')

    return jsonify(message='Show created successfully'), 201


@show_bp.route('/show/<int:show_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_show(show_id):
    show = Show.query.get(show_id)

    if not show:
        return jsonify(error='Show not found'), 404

    data = request.json
    name = data.get('name')
    tags = data.get('tags')
    ticket_price = data.get('ticket_price')
    theatre_id = data.get('theatre_id')
    youtube_url = data.get('youtube_url')
    date = data.get('show_date')
    language = data.get('language')


    timing_str = date
    show_date = datetime.strptime(timing_str, '%Y-%m-%dT%H:%M')
    
    if name:
        show.name = name
        # Retrieve movie information from the OMDB API
        omdb_api_key = os.environ.get("OMDB_API_KEY")
        movie_title = show.name  # Use the updated name
        omdb_url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&t={movie_title}"
        response = requests.get(omdb_url)
        movie_data = response.json()

        # Extract the desired movie information
        movie_description = movie_data.get('Plot')
        director = movie_data.get('Director')
        movie_length = movie_data.get('Runtime')
        image_url = movie_data.get('Poster')
        cast = movie_data.get('Actors')
        writer=movie_data.get('Writer')

        # Update the movie information in the show object
        show.movie_description = movie_description
        show.director = director
        show.movie_length = movie_length
        show.image_url = image_url
        show.cast = cast
        show.writer=writer

    if show_date:
        show.show_date = show_date
    if tags:
        show.tags = tags
    if ticket_price:
        show.ticket_price = ticket_price
    if theatre_id:
        theatre = Theatre.query.get(theatre_id)
        if not theatre:
            return jsonify(error='Theatre not found'), 404
        show.theatre_id = theatre_id
    if youtube_url and youtube_url != show.youtube:
        url = youtube_url
        video_id = re.search(r"youtu\.be\/(.+)", url)
        if video_id:
            video_id = video_id.group(1)
            show.youtube = video_id
        else:
            return jsonify(error='Video id not found')
    if language:
        show.language=language

    db.session.commit()
    
    # cache.delete_memoized('get_show', show_id)


    return jsonify(message='Show updated successfully')


@show_bp.route('/show/<int:show_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_show(show_id):
    show = Show.query.get(show_id)

    if not show:
        return jsonify(error='Show not found'), 404

    db.session.delete(show)
    db.session.commit()
    # cache.delete('all_shows')

    return jsonify(message='Show deleted successfully')


@show_bp.route('/show/<int:show_id>/vote', methods=['POST'])
@jwt_required()
def vote_show(show_id):
    data = request.json
    rating = data.get('rating')

    if rating is None:
        return jsonify(error='Rating value is missing'), 400

    show = Show.query.get_or_404(show_id)

    user_id = get_jwt_identity()['id']


    existing_vote = UserVote.query.filter_by(user_id=user_id, show_id=show_id).first()
    if existing_vote:
        return jsonify(error='You have already voted for this show'), 400

    user_vote = UserVote(user_id=user_id, show_id=show_id, rating=rating, voted_at=datetime.now())

    show.rating += rating
    show.num_votes += 1

    db.session.add(user_vote)
    db.session.commit()

    return jsonify(message='Vote recorded successfully'), 201

@show_bp.route('/show/<int:show_id>/comment', methods=['POST'])
@jwt_required()
def comment_show(show_id):
    data = request.json
    comment = data.get('comment')

    if comment is None:
        return jsonify(error='Comment value is missing'), 400
    
    show = Show.query.get_or_404(show_id)

    user_id = get_jwt_identity()['id']
    user = User.query.get(user_id)

    user_comment = UserComment(user_id=user_id, show_id=show_id, comment=comment, c_username=user.username, commented_at=datetime.now())
    db.session.add(user_comment)
    db.session.commit()
    return jsonify(message='Comment recorded successfully'), 201
