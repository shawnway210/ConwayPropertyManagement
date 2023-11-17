import react from 'react';


function Review({name, rating, comment}){
    return(
        <div>
            <h3>Name:</h3>
            <p>{name}</p>
            <h3>Rating:</h3>
            <p>{rating}</p>
            <h3>Comment:</h3>
            <p>{comment}</p>
        </div>
    )
}
export default Review