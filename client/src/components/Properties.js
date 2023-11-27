import React from 'react';
import Property from './Property'

// import NewPropertyForm from './NewPropertyForm';

function Properties({properties, setProperties, setImages, setReviews}){
console.log(properties)
    const mappedProperties = properties.map(property => (
    
        <Property
        key = {property.id}
        id = {property.id}
        name = {property.name}
        location = {property.location}
        description = {property.description}
        amenities = {property.amenities}
        availability = {property.availability}
        image = {property.image}
        reservation = {property.reservation}
        property = {property}
        properties = {properties}
        setProperties={setProperties}
        setImages={setImages}
        setReviews={setReviews}
        />

    ))

    return (
        <div>
            {mappedProperties}
        </div>
    )
}
export default Properties