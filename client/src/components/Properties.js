import react from 'react';
import Property from './Property'


function Properties({properties}){
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
        images = {property.images}
        reviews = {property.reviews}
        />

    ))

    return (
        <div>
            {mappedProperties}
        </div>
    )
}
export default Properties