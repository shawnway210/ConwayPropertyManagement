import React, { useState } from 'react';
import review from './Review';

function ReviewDetail({ comment, rating , setReviews, reviews}){

    const [showEditForm, setShowEditForm] = useState(false)
    const [editComment, setEditComment] = useState(comment)
    const [editRating, setEditRating] = useState(rating)

    const handleSubmit = (e) =>{
        e.preventDefault();

        const updatedReview = {
            method: "PATCH",
            headers: {
                "Content_Type": "application?json",
            },
            body: JSON.stringify({
                comment : editComment,
                rating : editRating
            }),
        };
        
        fetch(`/reviews/${review.id}`, updatedReview)
            .then((res) => res.json())
            .then(data => {
                const updatedReviews = reviews.map(review => {
                    if(review.id == data.id){
                        return( data,
                            window.location.reload())
                    }else{
                        return( review,
                    window.location.reload())
                    }
                })
                setReviews(updatedReviews)
                setShowEditForm(false)
            })
    }
    
    function handleDelete(id){
        const filteredReviews = reviews.filter(review =>{
            console.log(review)
            console.log(filteredReviews)
            return (review.id != id)
        })
        setReviews(filteredReviews)
        console.log(filteredReviews)
        fetch(`/reviews/${review.id}`,{
            method: "DELETE"
        })

        window.location.reload()
    }
    
    if (showEditForm){
        return (
            <div>
                <h3>Edit</h3>
                <form onSubmit = {handleSubmit}>
                    <input
                    label='Comment'
                    placeholder='Comment'
                    value={editComment}
                    onChange={(e) => setEditComment(e.target.value)}
                    />
                    <input
                    label='Rating'
                    placeholder='Rating'
                    value={rating}
                    onChange={(e) => setEditRating(e.target.value)}
                    />
                    <button type="submit">Submit</button>
                </form>
            </div>
        )
    }
    return( 
    <div>
        
        <p>{comment}</p>
        <p>{rating}</p>
   

    <button className='edit_review' onClick={() => setShowEditForm(!showEditForm)}> Edit Review</button>
    <button className='delete_review' onClick={() => handleDelete(review.id)}> Delete Reviw</button>
    </div>
    )
}

export default ReviewDetail