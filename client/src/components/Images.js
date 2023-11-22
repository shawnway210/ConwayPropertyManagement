import React from "react";
import Image from "./Image";
console.log("here")

function Images({images, setImages}){console.log(images)
    const mappedImages = images.map(image =>(
        
        <Image 
        key = {image.id}
        id = {image.id}
        image = {image.image}
        images = {images}
        setImages = {setImages}
        
        />
    
    ))

    return (
        <div>
            {mappedImages}
        </div>
    )
}
export default Images