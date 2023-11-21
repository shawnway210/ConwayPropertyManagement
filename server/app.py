#!/usr/bin/env python3

# Standard library imports
from flask import Flask, make_response, jsonify, request, session
# Remote library imports

from flask_restful import Resource
from flask_migrate import Migrate

# Local imports
from config import app, api, db
# Add your model imports
from models import  Property, Review, User, Image

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

@app.route('/signup', methods = ['POST'])
def signup():
    
    form_data = request.get_json()

    username = form_data['username']
    password = form_data['password']

    try:

        new_user = User(
            username = username
        )

        
        new_user.password_hash = password

        db.session.add(new_user)

        db.session.commit()

        
        session['user_id'] = new_user.id

        response = make_response(
            new_user.to_dict(),
            201
        )

    except:
        response = make_response(
            {"ERROR" : "Could not create user!"},
            400
        )

    return response
@app.route('/check_session', methods = ['GET'])
def check_session():
    
    user_id = session['user_id']

    user = User.query.filter(User.id == user_id).first()

    if user:
        response = make_response(
            user.to_dict(),
            200
        )

    else:
        response = make_response(
            {},
            404
        )

    return response

@app.route('/login', methods = ['POST'])
def login():
    
    form_data = request.get_json()

    username = form_data['username']
    password = form_data['password']

    user = User.query.filter(User.username == username).first()

    if user:
       
        is_authenticated = user.authenticate(password)

        if is_authenticated:
            session['user_id'] = user.id

            response = make_response(
                user.to_dict(),
                201
            )
        else:
            response = make_response(
                {"ERROR" : "USER CANNOT LOG IN"},
                400
            )
    else:
        response = make_response(
            {"ERROR" : "USER NOT FOUND"},
            404
        )

    return response



@app.route('/logout', methods = ['DELETE'])
def logout():
    
    session['user_id'] = None

    response = make_response(
        {},
        204
    )

    return response





@app.route('/properties', methods=['GET', 'POST'])
def properties():
    
    if request.method == 'GET':
        
        properties = Property.query.all()
       
        properties_dict = [property.to_dict(rules=('-property_users',)) for property in properties]

        response = make_response(
             properties_dict,
            200
        )

    elif request.method == 'POST':

        user = User.query.filter(User.id == session['user_id']).first()
        
        if user.role == 'Admin':

            request_json = request.get_json()

            name = request_json['name']
            location = request_json['location']
            description = request_json['description']
            amenities = request_json['amenities']
            availability = request_json['availability']
            reservation = request_json['reservation']
            image = request_json['image']

        
            db.session.add(property)
            db.session.commit()

            return property.to_dict(), 201
        try:
            
            property = Property(
                name=name,
                location=location,
                description=description,
                amenities=amenities,
                availability=availability,
                user_id=session['user_id'],
                reservation=reservation,
                image=image
            )

            db.session.add(property)
            db.session.commit()

            return property.to_dict(), 201
        
        except:

            return {'error': '422 Unprocessable Entity'} , 422
        
    return response
        


        

@app.route('/properties', methods=['DELETE'])
def property_by_id(id):
    property = Property.query.filter(Property.id == id).first()
    user = User.query.filter(User.id == session['user_id']).first()

    if user.role == "Admin":
        db.session.delete(property)
        db.session.commit()

        response = make_response(
            {}, 204
        )
        
        return response
    
    



@app.route('/reviews', methods=['GET','POST'])
def reviews():
    
    if request.method == 'GET':
        
        reviews = Review.query.all()

        reviews_dict = [review.to_dict() for review in reviews]
        
        response = make_response(
            reviews_dict,
            200
        )
        
        
    elif request.method == 'POST':

        try:

            form_data = request.get_json()

            new_review_obj = Review(

                name = form_data['name'],
                email = form_data['email'],
                rating = form_data['rating'],
                comment = form_data['comment'],
                property_id = form_data['property_id']
            )

            db.session.add(new_review_obj)
            db.session.commit()

            return new_review_obj.to_dict()
        
        except ValueError:

            return {'error': 'Review must have name, email, rating'}
    
    return response



@app.route('/reviews/<int:id>', methods=['PATCH','DELETE'])
def review_by_id(id):
    review = Review.query.filter(Review.id == id).first()

    if request.method == 'PATCH':

        try:

            form_data = request.get_json()

            for attr in form_data:
                setattr(review, attr, form_data.get(attr))
        
            db.session.commit()

            response = make_response(
                review.to_dict(),
                202
            )
        
        except ValueError:

            response = make_response(
                {"Review must have a name, email, rating"},
                400
            )
    
    elif request.method == 'DELETE':
        
        db.session.delete(review)
        db.session.commit()

        response = make_response(
            {}, 204
        )

    return response




@app.route('/images', methods=['GET', 'POST'])
def images():
    
    if request.method == 'GET':
        images = Image.query.all()

        images_dict = [image.to_dict() for image in images]
        
        response = make_response(
            images_dict,
            200
        )
        return response
    
    elif request.method == ['POST']:

            request_json = request.get_json()

            image = request_json['image']

            try:

                new_image = Image(
                    image=image,
                    user_id=session['user_id'],
                )

                db.session.add(new_image)
                db.session.commit

                return new_image.to_dict(), 201
            
            except:

                return {'error': '422 Unprocessable Entity'}, 422
        
        
    
    return response



@app.route('/images/<int:id>', methods=['DELETE'])
def images_by_id(id):
    image = Image.query.filter(Image.id == id).first()
    print(session)
       
    image = Image.query.filter(Image.id == id).first()

    user = User.query.filter(User.id == session['user_id']).first()

    if user.role == 'Admin':
        if image:
            db.session.delete(image)
            db.session.commit()

            response = make_response(
                {}, 204
            )
        
        else:
            response = make_response(
                {'error': 'Image not found'}, 404
            )
    return response





if __name__ == '__main__':
    app.run(port=5555, debug=True)

