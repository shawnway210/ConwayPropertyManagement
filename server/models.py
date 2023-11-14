from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)

# Models go here!
class Property(db.Model , SerializerMixin):
    __tablename__='properties'

    serialize_rules = ('-property_users.property', )
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    descritption = db.Column(db.String)
    amenities = db.Column(db.String)
    #availability_calender = db.Column(db.json)
    pricing_per_night_in_dollars = db.Column(db.Integer)
    images = db.Column(db.String)

    property_users = db.relationship('PropertyUser', back_populates='property', cascade='all, delete-orphan')

    availlability = db.relationship('Availability', back_populates='property', cascade='all, delete-orphan')
    

class Review(db.Model, SerializerMixin):
    __tablename__='reviews'

    serialize_rules = ('-property_users.review', )

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    property_users = db.relationship('PropertyUser', back_populates='review', cascade='all, delete-orphan')


class Reservation(db.Model, SerializerMixin):
    __tablename__='reservations'

    serialize_rules = ('-property_users.reservation', '-availabiltiy')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    check_in = db.Column(db.DateTime)
    check_out = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    #availability_calendar = db.Column(db.Json)
    
    property_users = db.relationship('User', back_populates='reservation', cascade='all, delete-orphan')

    availabilty = db.relationship('Availability', back_populates='reservation', cascade='all, delete-orphan')

class User(db.Model, SerializerMixin):
    __tablename__='users'

    serialize_rules = ('-property_users.user', )

    ROLES = [
        ('admin', 'Administrator'),
        ('visitor', 'Visitor'),
    ]


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String, default='visitor')

    property_users = db.relationship('PropertyUser', back_populates='user', cascade='all, delete-orphan')

class Availability(db.Model, SerializerMixin):
    __tablename__ = 'availability'

    serialize_rules = ('-reservation.availability', '-property.avaialbility')

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    status = db.Column(db.String) 
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'))
    reseevation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'))

    property = db.relationship('Property', back_populates='availability')

    reservation = db.relationship('Reservation', back_populates='availability')



class PropertyUser(db.Model, SerializerMixin):
    __tablename__='property_users'

    serialize_rules = ('-property.property_users', '-review.property_users', '-reservation.property_users', '-user.property_users')

    id = db.Column(db.Integer, primary_key=True)

    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'))
    use_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    revervation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'))
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))

    property = db.relationship('Property', back_populates='property_users')

    review = db.relationship('Review', back_populates='property_users')

    reservation = db.relationship('Reservation', back_populates='property_users')

    user = db.relationship('User', back_populates='property_users')

    



