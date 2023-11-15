#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Property, Review, Image, User
from flask import request
from datetime import datetime

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Nuking the database....")
        
        
        # Delete all existing records from the tables
        db.session.query(Property).delete()
        db.session.query(Review).delete()
        db.session.query(Image).delete()
        db.session.query(User).delete()


        print("Starting seed...")


        #Create and seed the Properties
        print('Picking Properties...')

        properties = [
            Property(
                id = 1,
                name = 'Phat Phish',
                location = 'Oak Island, North Carolina',
                description = "There's nothing better than having the ocean as your front yard, and that's exactly what you get at this ocean front oasis. The sound of the waves will drift you off to sleep. Take in the views from the ocean front deck, the beach is right dow the front steps!",
                amenities = "4 bedrooms One King bedroom, 2 full bedrooms, and one room with two twin beds. All rooms have TV and Roku, except the kids room. 2 full bathrooms, each with a tub Full kitchen with plenty of cookware and serving dishes. Blender, Kuerig, coffee maker, toaster, microwave. Dining table for 6 Nice living room with full ocean view right from the couch. Or the recliner! Decisions, decisions. Roku TV",
                availability = 'https://www.airbnb.com/calendar/ical/738948885345971986.ics?s=7dc124552a0de7b6db90111cf65ab513',
            ),

            Property(
                id = 2,
                name = 'Slope Slider #6',
                location = 'Suger Mountain',
                description = 'With the ski slope out the front door it does not get much better than this. With ski-in /ski-out access this original Sugar Mountain slopesider cabin is a mountain dream escape. Watch the action on the slopes from the porch or inside with the floor to ceiling windows. There is even a cozy wood burning fire place. In the fall this is the perfect retreat to take in the autumnal colors while you spend your days sightseeing along the parkway. This circular treetop cabin has floor to ceiling windows and an open floorplan in the kitchen, living and dining room making you feel as if you are in a tree-top hideaway. There is a wood burning fireplace that is the heart of the home and a spiral staircase (and baby gate!) leading to the lower level with the laundry room, mudroom and ski slope access.  When there is snow on the roads you will need a 4WD vehicle to access the property.',
                amenities = 'Two Bedrooms, Two Bathrooms, living room, woodstove, a tv in each room, dining space with coffee station, fully equipped kitchen, Deck, Ski room with table and chairs, ski racks, ski in/out entrance from slope.',
                availability = 'https://www.airbnb.com/calendar/ical/731915024153813910.ics?s=bbaaa95eef6b88b7d6286b82d0745214',
            ),
        ]


        db.session.add_all(properties)
        db.session.commit()


        reviews = []


        db.session.add_all(reviews)
        db.session.commit()


        users = []

        db.session.add_all(users)
        db.session.commit()



        images = []

        db.session.add_all(images)
        db.session.commit()

        

        