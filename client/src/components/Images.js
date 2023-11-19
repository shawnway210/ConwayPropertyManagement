import React from "react";
import Image from "./Image";


function Images({images}){
    const mappedImages = images.map(image =>(
        <Image 
        key = {image.id}
        id = {image.id}
        image = {image.image}
        />
    ))

    return (
        <div>
            {mappedImages}
        </div>
    )
}
export default Images