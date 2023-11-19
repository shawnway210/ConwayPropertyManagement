import React from 'react';
import Review from './Review';

function Reviews({reviews}){
    const mappedReviews = reviews.map(review => (
       <Review
       key = {review.id}
       id = {review.id}
       name = {review.name}
       rating = {review.rating}
       comment = {review.comment}
       property = {review.property.name}
       />
    ))
    
    return (
        <div>
            {mappedReviews}
        </div>
    )
}
export default Reviews