from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime
from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)

# Models go here!
class Property(db.Model , SerializerMixin):
    __tablename__='properties'

    serialize_rules = ('-property_users.property', '-availability.property')
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    descritption = db.Column(db.String)
    amenities = db.Column(db.String)
    images = db.Column(db.String)

    property_users = db.relationship('PropertyUser', back_populates='property', cascade='all, delete-orphan')

    availlability = db.relationship('Availability', back_populates='property', cascade='all, delete-orphan')

    @validates('name')
    def validates_name(self, key, name):
        if name:
            return name
        else:
            raise ValueError("The property must have a name.")
    
    @validates('address')
    def validates_address(self, key, address):
        if address:
            return address
        else:
            raise ValueError("The property must have an address.")
        
    @validates('description')
    def validates_description(self, key, description):
        if description:
            return description
        else:
            raise ValueError("The property must have a description.")
        
    @validates('images')
    def validates_images(self, key, images):
        if images:
            return images
        else:
            raise ValueError("The property must have images.")

    

class Review(db.Model, SerializerMixin):
    __tablename__='reviews'

    serialize_rules = ('-property_users.review', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    property_users = db.relationship('PropertyUser', back_populates='review', cascade='all, delete-orphan')

    @validates('name')
    def validates_name(self, key, name):
        if name:
            return name
        else:
            raise ValueError("The review must have name.")
        
    @validates('email')
    def validates_email(self, key, email):
        if email:
            return email
        else:
            raise ValueError("The review must have an email.")
        
    @validates('rating')
    def validates_rating(self, key, rating):
        if 0 <= rating <= 5:
            return rating
        else:
            raise ValueError("The reviews rating must btween 0 and 5 ,inclusively.")
        


class Reservation(db.Model, SerializerMixin):
    __tablename__='reservations'

    serialize_rules = ('-property_users.reservation', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    airbnb_link = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    property_users = db.relationship('User', back_populates='reservation', cascade='all, delete-orphan')

    @validates('name')
    def validates_name(self, key, name):
        if name:
            return name
        else:
            raise ValueError("Reservation must have name.")
        
    @validates('email')
    def validates_email(self, key, email):
        if email:
            return email
        else:
            raise ValueError("Reservation must have an email.")



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

    @validates('username')
    def validates_username(self, key, username):
        if 0 < len(username) < 20:
            return username
        else:
            raise ValueError("The username must be betwen 0 and twenty characters.")
    
    
        


class Availability(db.Model, SerializerMixin):
    __tablename__ = 'availability'

    serialize_rules = ('-reservation.availability', '-property.avaialbility')

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    status = db.Column(db.String) 
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'))

    property = db.relationship('Property', back_populates='availability')



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

    



