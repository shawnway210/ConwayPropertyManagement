import React from 'react';



function Property({name, location, description, amenities, availability, image, properties, setProperties, reservation, id}){

    
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
        </div>
    )
}
export default Property