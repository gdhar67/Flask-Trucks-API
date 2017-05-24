from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/truck'
db = SQLAlchemy(app)



# Each class represents a table.

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    account_type = db.Column(db.String(255), nullable=False)
    user_trucks = db.relationship('user_trucks', backref='user_trucks', lazy='dynamic')
    booking_requests = db.relationship('booking_requests', backref='booking_user', lazy='dynamic')
    journey_plans = db.relationship('journey_plans', backref='journey_user', lazy='dynamic')



class user_trucks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    truck_name = db.Column(db.String(255), nullable=False)
    number_plate = db.Column(db.String(255), unique=True)
    max_weight = db.Column(db.String(255), nullable=False)
    max_volume = db.Column(db.String(255), nullable=False)
    current_city = db.Column(db.String(255), nullable=False)
    percent_volume_left = db.Column(db.Float(2), server_default="100")
    percent_weight_left = db.Column(db.Float(2), server_default="100")
    journey_plans = db.relationship('journey_plans', backref='journey_truck', lazy='dynamic')



class truck_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    truck_name = db.Column(db.String(255), nullable=False)
    max_weight = db.Column(db.Float(2), nullable=False)
    max_volume = db.Column(db.Float(2), nullable=False)

    

class booking_requests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    source = db.Column(db.String(255), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    total_volume = db.Column(db.String(255), nullable=True)
    total_weight = db.Column(db.String(255), nullable=True)
    pickup_date = db.Column(db.Date, nullable=False)
    pickup_time = db.Column(db.Time, nullable=False)
    dropoff_date = db.Column(db.Date, nullable=False)
    dropoff_time = db.Column(db.Time, nullable=False)
    journey_plans = db.relationship('journey_plans', backref='journey_booking', lazy='dynamic') 
    items = db.relationship('items', backref='items', lazy='dynamic') 



class items(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	booking_request_id = db.Column(db.Integer, db.ForeignKey('booking_requests.id'))
	item_name = db.Column(db.String(255), nullable=False)
	weight = db.Column(db.Float(2), nullable=False)
	height = db.Column(db.Float(2), nullable=False)
	length = db.Column(db.Float(2), nullable=False)
	breadth = db.Column(db.Float(2), nullable=False)
	volume = db.Column(db.Float(2), nullable=False)



class journey_plans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    booking_requests_id = db.Column(db.Integer, db.ForeignKey('booking_requests.id'))
    truck_id = db.Column(db.Integer, db.ForeignKey('user_trucks.id'))
    space_allocation = db.Column(db.String(255), nullable=False)
    end_to_end = db.Column(db.String(255), nullable=False)
    source = db.Column(db.String(255), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    total_no_of_items = db.Column(db.Integer, nullable=False)
    pickup_date = db.Column(db.Date, nullable=False)
    pickup_time = db.Column(db.Time, nullable=False)
    dropoff_date = db.Column(db.Date, nullable=False)
    dropoff_time = db.Column(db.Time, nullable=False)
    journey_fare = db.Column(db.Float(2), nullable=False)
    status = db.Column(db.String(255), nullable=False)
