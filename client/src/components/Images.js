import React from "react";
import Image from "./Image";


function Images({images, setImages}){
    const mappedImages = images.map(image =>(
        <Image 
        key = {image.id}
        id = {image.id}
        image = {image}
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