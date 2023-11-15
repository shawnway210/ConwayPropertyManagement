#!/usr/bin/env python3

# Standard library imports
from flask import Flask, make_response, jsonify, request
# Remote library imports
from flask import request
from flask_restful import Resource
from flask_migrate import Migrate

# Local imports
from config import app, api
# Add your model imports
from models import db, Property, Review, User, PropertyUser, Image

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'



@app.route('/properties', methods=['GET'])
def properties():
    properties = Property.query.all()

    response = make_response(
        properties.to_dict(),
        200
    )
    return response



@app.route('/reviews', methods=['GET'])
def reviews():
    reviews = Review.query.all()

    response = make_response(
        reviews.to_dict(),
        200
    )
    return response



@app.route('/images', methods=['GET'])
def images():
    images = Image.query.all()

    response = make_response(
        images.to_dict(),
        200
    )
    return response















if __name__ == '__main__':
    app.run(port=5555, debug=True)

