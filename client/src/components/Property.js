import React from 'react';
import { useHistory } from 'react-router-dom';





function Property({name, location, description, amenities, availability, image, properties, setProperties, reservation, setImages, setReviews, setReview, id}){

    const history = useHistory();

    const handleClick1 =() => {
        history.push(`/properties/${id}/images`)
    }

    const handleClick2 =() => {
        history.push(`/properties/${id}/reviews`)
    }

    const handleClick3 =() => {
        history.push("/newreview")
    }

    
    function handleDelete(id){
    
    fetch(`/properties/${id}`, {
            method: "DELETE"
        })
        .then(() => {
            const filteredProperties = properties.filter(property => {
        
            return (property.id !== id)
        })
        setProperties(filteredProperties)
        })

    }
    return (
        <div>
            <p className='property-name'>{name}</p>
            <img className='property-img' src = {image} alt = {name}/>
            <h2>Location:</h2>
            <p>{location}</p>
            <h2>Description:</h2>
            <p>{description}</p>
            <h2>Amnenties:</h2>
            <p>{amenities}</p>
            <h3>Availability:</h3>
            <p>{availability}</p>
            <h3>Reservation</h3>
            <p>{reservation}</p>
            <button className='delete_property' onClick={() => handleDelete(id)}>Delete</button>
            <button onClick={handleClick1} type="button">Images</button>
            <button onClick={handleClick2} type="button">Reviews</button>
            <button onClick={handleClick3} type="button">Please Leave A Review</button>
        </div>
    )
}
export default Property