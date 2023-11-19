import React from 'react';


function Property({name,location,description,amenities,availability, image, property, mappedProperties, setProperties}){
    
    function handleDelete(id){
    const filteredProperties = mappedProperties.filter(property => {
        
        return (property.id !== id)
    })
    setProperties(filteredProperties)
    fetch(`/properties/${property.id}`, {
            method: "DELETE"
        })
        window.location.reload()
    }


    return (
        <div>
            <h1>Name:</h1>
            <p>{name}</p>
            <img src = {image} alt = {name}/>
            <h2>Location:</h2>
            <p>{location}</p>
            <h2>Description:</h2>
            <p>{description}</p>
            <h2>Amnenties:</h2>
            <p>{amenities}</p>
            {/* <h3>Reviews</h3>
            <p>{reviews}</p> */}
            <h3>Availability:</h3>
            <p>{availability}</p>
            {/* <h3>Images</h3>
            <p>{images}</p> */}

            <button className='delete_property' onClick={() => handleDelete(property.id)}>Delete</button>
        </div>
    )
}
export default Property