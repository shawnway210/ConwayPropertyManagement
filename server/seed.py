#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Property, Review, Image, User, PropertyUser


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
                name = 'Phat Phish',
                location = 'Oak Island, North Carolina',
                description = "There's nothing better than having the ocean as your front yard, and that's exactly what you get at this ocean front oasis. The sound of the waves will drift you off to sleep. Take in the views from the ocean front deck, the beach is right dow the front steps!",
                amenities = "4 bedrooms One King bedroom, 2 full bedrooms, and one room with two twin beds. All rooms have TV and Roku, except the kids room. 2 full bathrooms, each with a tub Full kitchen with plenty of cookware and serving dishes. Blender, Kuerig, coffee maker, toaster, microwave. Dining table for 6 Nice living room with full ocean view right from the couch. Or the recliner! Decisions, decisions. Roku TV",
                availability = 'https://www.airbnb.com/calendar/ical/738948885345971986.ics?s=7dc124552a0de7b6db90111cf65ab513',
            ),

            Property(
                name = 'Slope Slider #6',
                location = 'Sugar Mountain, North Carolina',
                description = 'With the ski slope out the front door it does not get much better than this. With ski-in /ski-out access this original Sugar Mountain slopesider cabin is a mountain dream escape. Watch the action on the slopes from the porch or inside with the floor to ceiling windows. There is even a cozy wood burning fire place. In the fall this is the perfect retreat to take in the autumnal colors while you spend your days sightseeing along the parkway. This circular treetop cabin has floor to ceiling windows and an open floorplan in the kitchen, living and dining room making you feel as if you are in a tree-top hideaway. There is a wood burning fireplace that is the heart of the home and a spiral staircase (and baby gate!) leading to the lower level with the laundry room, mudroom and ski slope access.  When there is snow on the roads you will need a 4WD vehicle to access the property.',
                amenities = 'Two Bedrooms, Two Bathrooms, living room, woodstove, a tv in each room, dining space with coffee station, fully equipped kitchen, Deck, Ski room with table and chairs, ski racks, ski in/out entrance from slope.',
                availability = 'https://www.airbnb.com/calendar/ical/731915024153813910.ics?s=bbaaa95eef6b88b7d6286b82d0745214',
            ),
        ]


        db.session.add_all(properties)
        db.session.commit()


        reviews = [
            Review(
                name = 'Selena',
                email = 'N/A',
                rating = 5,
                comment = "Porter's instructions were super helpful and straight forward. Easy to find the place, key, surrounding places, recommendations, trash hut. Loved all the antiques. Very nice location with an even nicer view!",
                property_id = 2
            ),

            Review(
                name = 'Sarah',
                email = 'N/A',
                rating = 5,
                comment = "Super cute house! Very cozy and clean. We would definitely stay again!",
                property_id = 2
            ),

            Review(
                name ='Gary',
                email = 'N/A',
                rating = 5,
                comment = "Our stay was very nice. Would look forward to a ski season visit. Easy access to the ski slopes.",
                property_id = 2,
            ),

            Review(
                name = 'Caleb',
                email = 'N/A',
                rating = 5,
                comment = "Nice clean space",
                property_id = 2,
            ),
            
            Review(
                name = 'Felicia',
                email = 'N/A',
                rating = 4,
                comment = "If you love to ski, this house will be perfect for you! It is located right on a ski lift hill! The home is older but the host is in the process of updating. The home is quaint and cozy. The beds were very comfortable and bed linens high quality. The bathrooms are small but in line with the time when this home was designed. There are tvs in every room and a nice lower level for hanging out. The rental price of the home reflects it being older so that makes it a good deal because rentals in this area are HIGH. The house was very convenient to all the places we were exploring including Autumn At Oz on Beech Mountain, the Banner Elk Winery, Grandfather Mountain Winery, and Mast General Store. The host was a pleasure to work with and we would definitely work with her again!",
                property_id = 2,
            ),

            Review(
                name = 'Brittany',
                email = 'N/A',
                rating = 4,
                comment = "It was a great stay. I was nervous about bringing my 8 month old, as there were stairs, but there was a baby gate ziptied to the top. the view from the patio was amazing, and on the weekend, we got to watch the ski lift running for mountain bikers, as it's off-season.The pictures do seem brighter than it actually is, but we didn't mind. Wifi was great, and cell service was surprisingly not an issue at the location. We went in the middle of July, and the fans and open windows were adequate for cooling us. Beware - There are a couple of holes in the driveway that are not easily seen as they are covered in grass, and my husband hurt his ankle by stepping in one while carrying in our luggage. It wasn't sprained, but we had gone there so he could play golf and was in too much pain to do so. Overall, I was very happy with this this place!",
                property_id = 2,
            ),

            Review(
                name = 'Kendall',
                email = 'N/A',
                rating = 5,
                comment = "The only downfall was that the Hulu remote didn't work. Honestly, it is more of a me not reading the description and reviews fully. Either way, the house is right down the road from plenty of attractions and places to eat! The firework show we watched from the balcony was the icing on the cake.",
                property_id = 2,
            ),

            Review(
                name = 'Michele',
                email = 'N/A',
                rating = 3,
                comment = "I felt like the pictures had been edited, to be very white, bright. House needs to be updated. Was disappointed when I arrived, but all turned out to be good. Host responded very quickly. Loved the view. Got to see some wildlife outside of house. Overall, was a good weekend. It was a good house, would stay here again.",
                property_id = 2,
            ),

            Review(
                name = 'Heidi',
                email = 'N/A',
                rating = 5,
                comment = "The location was perfect for our planned hikes, and the kitchen had everything we needed to enjoy cooking during our stay.",
                property_id = 2,
            ),

            Review(
                name = 'Martin',
                email = 'N/A',
                rating = 4,
                comment = "Great ski in/out spot. About 30M from main Sugar Mountain Resort lift. Quiet area, and only 8 minutes away from a big supermarket. The house is well located and cozy, but needs a renewal and modernization (Netflix, better plugs, and proper heating devices are a must!).",
                property_id = 2,
            ),

            Review(
                name = 'Steven',
                email = 'N/A',
                rating = 5,
                comment = "The location was perfect, the cabin was cozy and well stocked. Thank you Porter.",
                property_id = 2,
            ),

            Review(
                name = 'Tyler',
                email = 'N/A',
                rating = 5,
                comment = "Perfect location for ski in ski out beautiful view of the slope and felt very cozy and just like home, definitely will be looking to stay at this location many more times",
                property_id = 2,
            ),

            Review(
                name = 'Robert',
                email = 'N/A',
                rating = 5,
                comment = "Great and cozy place with ski in/out access.",
                property_id = 2,
            ),

            Review(
                name = 'Yuanshan',
                email = 'N/A',
                rating = 5,
                comment = "Love the communications. Nice to ski at Sugar Mountain!",
                property_id = 2,
            ),

            Review(
                name = 'Martin',
                email = 'N/A',
                rating = 5,
                comment = "We had an excellent stay. Will definitely be back.",
                property_id = 2,
            ),

            Review(
                name = 'Kelly',
                email = 'N/A',
                rating = 5,
                comment = "The best host! You will have a great experience by staying in this cabin",
                property_id = 2,
            ),

            Review(
                name = 'Andre',
                email = 'N/A',
                rating = 5,
                comment = "Our stay was wonderful with beautiful location and scenery. Great place to stay during any season.",
                property_id = 2,
            ),

            Review(
                name = 'Anna',
                email = 'N/A',
                rating = 5,
                comment = "It was a great space and perfect for the weekend we had planned to go up to Grandfather mountain",
                property_id = 2,
            ),

            Review(
                name = 'Rhonda',
                email = 'N/A',
                rating = 5,
                comment = "A beautiful view!! Spent hours on the porch.",
                property_id = 1,
            ),

            Review(
                name = 'Laura',
                email = 'N/A',
                rating = 5,
                comment = "WONDERFUL TIME AS ALWAYS!!!!!!!!!!!!",
                property_id = 1,
            ),

            Review(
                name = 'Matthew',
                email = 'N/A',
                rating = 5,
                comment = "Great house enjoyed the stay will be back next year",
                property_id = 1,
            ),

            Review(
                name = 'Elyse',
                email = 'N/A',
                rating = 5,
                comment = "This is a great spot. Super comfy, great big windows for viewing the beach, close to restaurants/grocery store, and for us (with a toddler) having a one-story space was perfect. We had great weather, but for rainy days, there is a really cute hangout spot under the house that we definitely would have appreciated. The house is decorated in a very fun way, and my toddler had a really great time asking questions about EVERY SINGLE ITEM :) Thanks for the great stay!",
                property_id = 1,
            ),

            Review(
                name = 'Harriet',
                email = 'N/A',
                rating = 4,
                comment = "The house is older, yet full of personality. A very fun, retro vibe. The view cannot be beat. Period. And the house is right beside the roped access over the dunes. If you want a newly remodeled house full of granite, tile, etc...this is not that. If you like quaint places with a lot of spirit, and killer view, this is it. The house was clean. Well appointed with salt and pepper and coffee filter kinds of things. Nice enough towels and linens. Porter was great to work with.",
                property_id = 1,
            ),

            Review(
                name = 'Terri',
                email = 'N/A',
                rating = 5,
                comment = "My husband and I had a great stay at Phat Fish with our toddler. The ocean views were amazing and loved the convenience of just walking down the steps and out to the beach. The house could use a little TLC, but it was very clean and had everything we needed. We did find a couple cockroaches, but I think that is just a NC or southeast thing and not a cleanliness factor because the house was super clean. Porter is a great host as instructions and response time were clear and prompt. Made some great family memories during our stay!",
                property_id = 1,
            ),

            Review(
                name = 'Sarah',
                email = 'N/A',
                rating = 5,
                comment = "This area is AMAZING and this house worked great for our family of 7! Thank you Porter!",
                property_id = 1,
            ),

            Review(
                name = 'Allison',
                email = 'N/A',
                rating = 4,
                comment = "Absolutely amazing location! You literally step off the back steps onto the beach. The place was fine, but definitely in need of some TLC. Worth overlooking for the location though!",
                property_id = 1,
            ),

            Review(
                name = 'Sarah Beth',
                email = 'N/A',
                rating = 5,
                comment = "We really enjoyed our stay. Right on the beach and a beautiful view of the ocean. Perfect place for a relaxing vacation!",
                property_id = 1,
            ),

            Review(
                name = 'John',
                email = 'N/A',
                rating = 5,
                comment = "Absolutely nothing negative to say. Really quaint beach house nicely decorated and perfect for our family. We would definitely stay there again",
                property_id = 1,
            ),

            Review(
                name = 'Margot',
                email = 'N/A',
                rating = 5,
                comment = "Fabulous location right on the beach ! Charming older beach cottage with great eclectic decor! Felt really like a home and the location cannot be beat!",
                property_id = 1,
            ),

            Review(
                name = 'Annette',
                email = 'N/A',
                rating = 5,
                comment = "Nice and clean and had everything you need! Enjoyed our weekend with the beautiful view!!",
                property_id = 1,
            ),

            Review(
                name = 'Laura',
                email = 'N/A',
                rating = 5,
                comment = "Amazing wonderful Beach Front Cottage will be back for SURE!",
                property_id = 1,
            ),

            Review(
                name = 'Sarah',
                email = 'N/A',
                rating = 5,
                comment = "Location was amazing and the perfect stay for our family for the OI marathon! Porter provided great tips for things to do before/after!",
                property_id = 1,
            ),

            Review(
                name = 'Sean',
                email = 'N/A',
                rating = 5,
                comment = "Loved it, would go back!",
                property_id = 1,
            ),

            Review(
                name = 'Gregory',
                email = 'N/A',
                rating = 5,
                comment = "It was a lot of fun! Great trip!",
                property_id = 1,
            ),

            Review(
                name = 'Lonnie',
                email = 'N/A',
                rating = 5,
                comment = "This house is in a great location. The house was clean and stocked with everything needed. We enjoyed ourselves and will most definitely come back to stay here.",
                property_id = 1,
            ),

            Review(
                name = 'Brent',
                email = 'N/A',
                rating = 5,
                comment = "great location the rocking chairs on the porch were nice",
                property_id = 1,
            ),

            Review(
                name = 'Roz',
                email = 'N/A',
                rating = 5,
                comment = "Cute place, can't beat the location. South facing so you get both sunrise and sunset. We had a short stay but really enjoyed Oak Island",
                property_id = 1,
            ),

            Review(
                name = 'Nick',
                email = 'N/A',
                rating = 5,
                comment = "Such a cool beach house! Everything was clean and as described. Porter was quick to respond with any questions and made our stay great! I don’t think I have ever stayed so close to the beach. The view is beautiful!",
                property_id = 1,
            ),

            Review(
                name = 'Paul',
                email = 'N/A',
                rating = 5,
                comment = "We had a great time. The communication was super easy and quick and the place looks exactly like it does on the pictures. The neighborhood is very conveniently located. You can enjoy the beautiful sunrise colors and the sunset by the beach. Would absolutely recommend to stay there!",
                property_id = 1,
            ),

            Review(
                name = 'Wanda',
                email = 'N/A',
                rating = 5,
                comment = "All I all I enjoyed the stay Although the structure could use some better upkeep as far as lighting and electrical outlets that are coming out of the wall and sparking fire when you plug and unplug things. The back deck isn’t stable. It needs better upkeep",
                property_id = 1,
            ),
        ]



        db.session.add_all(reviews)
        db.session.commit()


        users = [
            User(
                username = 'Porter13',
                password = 'SkyWalker2015*',
                role = 'Admin',
            ),

            User(
                username = 'TooRude420',
                password = 'Bacio210!',
                role = 'visitor',
            ),

            User(
                username = 'SugarBritches3',
                password = 'Blaah21$',
                role = 'visitor'
            ),
        ]
            

        db.session.add_all(users)
        db.session.commit()

        



        images = []

        db.session.add_all(images)
        db.session.commit()




        property_users = [
            PropertyUser(
               property_id = 1,
               user_id = 2,
            ),

            PropertyUser(
                property_id = 2,
                user_id = 3,
            ),
        ]

        db.session.add_all(property_users)
        db.session.commit()

        

        