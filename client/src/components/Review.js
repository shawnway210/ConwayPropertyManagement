import React from 'react';


function Review({ name, rating, comment, property },){
    


    return(
        <div>
            <h3>Name:</h3>
            <p>{name}</p>
            <h3>Rating:</h3>
            <p>{rating}</p>
            <h3>Comment:</h3>
            <p>{comment}</p>
            <h3>Property</h3>
            <p>{property}</p>
        </div>
    )
}
export default Review