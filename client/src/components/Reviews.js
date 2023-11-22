import React from 'react';
import Review from './Review';
// import NewReviewForm from './NewReviewForm';
function Reviews({reviews, setReviews}){
    const mappedReviews = reviews.map(review => (
       <Review
       key = {review.id}
       id = {review.id}
       name = {review.name}
       rating = {review.rating}
       comment = {review.comment}
       property = {review.property.name}
       review = {review}
       setReviews = {setReviews}
       />
        
    ))
    console.log(mappedReviews)
    return (
        <div>
            {mappedReviews}
        </div>
    )
}
export default Reviews