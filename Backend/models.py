from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Theatre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    place = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    shows = db.relationship('Show', backref='theatre', lazy=True, cascade='all, delete')


class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, default=0.0)
    num_votes = db.Column(db.Integer, default=0)
    tags = db.Column(db.String(200))
    language = db.Column(db.String(200))
    ticket_price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(200))
    show_date = db.Column(db.DateTime, nullable=False)
    movie_description = db.Column(db.String(500))
    movie_length = db.Column(db.String(100))
    director = db.Column(db.String(200))
    writer = db.Column(db.String(200))
    image_url = db.Column(db.String(500))
    cast = db.Column(db.String(200))
    youtube = db.Column(db.String(200))
    theatre_id = db.Column(db.Integer, db.ForeignKey('theatre.id'), nullable=False)
    bookings = db.relationship('Booking', backref='show', lazy=True, cascade='all, delete')
    votes = db.relationship('UserVote', backref='show', lazy=True, cascade='all, delete')
    comments = db.relationship('UserComment', backref='show', lazy=True, cascade='all, delete')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    bookings = db.relationship('Booking', backref='user', lazy=True)
    votes = db.relationship('UserVote', backref='user', lazy=True)
    comments = db.relationship('UserComment', backref='user', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    movie_name = db.Column(db.String(200), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)


class UserVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    voted_at = db.Column(db.DateTime, nullable=False)


class UserComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)
    c_username = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(500), nullable=False)
    commented_at = db.Column(db.DateTime, nullable=False)


