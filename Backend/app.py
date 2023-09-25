from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import db, User, Booking, Show, Theatre
from theaters import theater_bp
from shows import show_bp
from auth import auth_bp
from bookings import booking_bp
from config import Config
from user import user_bp
from flask_mail import Mail, Message
from datetime import datetime, timedelta
from celery.schedules import crontab
from io import StringIO
from jinja2 import Environment, FileSystemLoader
from workers import make_celery, cache
import pandas as pd

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r'/*': {'origins': '*'}})

app.config["JWT_SECRET_KEY"] = app.config.get("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = app.config.get("JWT_ACCESS_TOKEN_EXPIRES")
app.config["JWT_TOKEN_LOCATION"] = app.config.get("JWT_TOKEN_LOCATION")

app.config['MAIL_SERVER'] = app.config.get('MAIL_SERVER')
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = app.config.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = app.config.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = app.config.get('MAIL_DEFAULT_SENDER')

app.config['CACHE_TYPE'] = "RedisCache"

cache.init_app(app)

db.init_app(app)
with app.app_context():
    db.create_all()

jwt = JWTManager(app)

celery = make_celery(app)

mail = Mail(app)

app.register_blueprint(theater_bp)
app.register_blueprint(show_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(booking_bp)
app.register_blueprint(user_bp)

############################################

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # sender.add_periodic_task(crontab(hour=19, minute=15), visit_reminder.s())
    # sender.add_periodic_task(crontab(day_of_month=1, hour=0, minute=0), send_monthly_report.s())
    sender.add_periodic_task(crontab(hour=5, minute=14), send_monthly_report.s())
    sender.add_periodic_task(crontab(hour=3, minute=47), visit_reminder.s())

@celery.task()
def visit_reminder():
    # users who haven't visited/booked recently (adjust the timedelta as needed)
    # threshold = datetime.utcnow() - timedelta(days=3)
    # users_to_remind = User.query.filter(User.bookings.any(Booking.booking_date <= threshold)).all()

    # users who haven't booked in the past 5 minutes
    # threshold = datetime.utcnow() - timedelta(minutes=5)
    # users_to_remind = User.query.filter(User.bookings.any(Booking.booking_date <= threshold)).all()

    # users who haven't booked today
    today = datetime.utcnow().date()
    users_to_remind = User.query.filter(User.bookings.any(Booking.booking_date <= today)).all()

    for user in users_to_remind:
        send_reminder(user)

    return f"Sent {len(users_to_remind)} reminders"
    
def send_reminder(user):
    with mail.connect() as conn:
        msg = Message(
            subject="Visit and Book Reminder - Ticket Show",
            recipients=[user.email],
            sender="fake.sandeep3@gmail.com"  
        )
        msg.body = f"Hello {user.username},\n\nDon't forget to visit and book a show on Ticket Show today!\n\nRegards,\nThe Ticket Show Team"
        conn.send(msg)

@celery.task()
def send_monthly_report():

    # list of users to send the report to (in this case, all admins)
    # users_to_notify = User.query.filter_by(is_admin=True).all()
    users_to_notify = User.query.all()

    with mail.connect() as conn:
        for user in users_to_notify:
            today = datetime.utcnow()
            start_of_month = datetime(today.year, today.month, 1)
            end_of_month = datetime(today.year, today.month + 1, 1) - timedelta(days=1)
            shows_booked = Booking.query.filter(Booking.user_id == user.id, Booking.booking_date >= start_of_month, Booking.booking_date <= end_of_month).all()
            shows_seen = []
            for booking in shows_booked:
                shows_seen.append(Show.query.filter_by(id=booking.show_id).first())
            total_revenue = sum(booking.amount for booking in shows_booked)

            env = Environment(loader=FileSystemLoader('templates'))
            template = env.get_template('monthly_report.html')
            mail_html = template.render(username=user.username, shows_seen=shows_seen, shows_booked=shows_booked, total_revenue=total_revenue, start_date=start_of_month.strftime('%B %d, %Y'), end_date=end_of_month.strftime('%B %d, %Y'))

            msg = Message(
                subject="Monthly Entertainment Report - Ticket Show",
                recipients=[user.email],
                sender="fake.sandeep3@gmail.com",
                html=mail_html
            )
            conn.send(msg)

        return f"Sent monthly reports to {len(users_to_notify)} users"
    
@celery.task(name="export_theatre_data")
def export_theatre_data(theatre_id):
    admin = User.query.filter_by(is_admin=True).first()
    shows = Show.query.filter_by(theatre_id=theatre_id).all()
    theater = Theatre.query.filter_by(id=theatre_id).first()
    columns = ['ShowId', 'Show_Name', 'Rating', 'Total_Rating', 'Show_Date', 'Ticket_Price', 'Total_Bookings', 'Total_Amount']
    output = []
    for show in shows:
        total_bookings = get_total_bookings(show.id)
        total_amount = total_bookings * show.ticket_price
        output.append([show.id, show.name, show.rating, show.num_votes, show.show_date, show.ticket_price, total_bookings, total_amount])

    theater_export = pd.DataFrame(output, columns=columns)
    csv_stream = StringIO()
    theater_export.to_csv(csv_stream, index=False)

    msg = Message(
        subject="Theater Report - Ticket Show",
        recipients=[admin.email],
        sender="fake.sandeep3@gmail.com",
    )

    msg.body = f'Theater Report For {theater.name}'
    msg.attach(f'{theater.name}.csv', 'text/csv', csv_stream.getvalue())
    mail.send(msg)

    return f"Sent monthly reports to {admin.email}"
    # return f"Sent monthly reports to {theatre_id}"


def get_total_bookings(show_id):
    bookings = Booking.query.filter_by(show_id=show_id).all()  
    total_bookings = sum(booking.quantity for booking in bookings)    
    return total_bookings

@app.get('/export_data/<int:theatre_id>')
def data_export(theatre_id):
    export_theatre_data.delay(theatre_id)
    return jsonify(message="CSV file sent to admin email"), 200

############################################

if __name__ == '__main__':
    app.run(
        host=app.config.get("FLASK_RUN_HOST"),
        port=app.config.get("FLASK_RUN_PORT"),
        debug=True
    )
