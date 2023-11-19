import React from "react";


function Image({mappedImages, image, id, setImages}){

    function handleDelete(id){
        const filteredImages = mappedImages.filter(image =>{
            console.log(image)
            console.log(id)
            return (image.id !== id)
        })
        setImages(filteredImages)
        console.log(filteredImages)
        fetch(`/images/${id}`,{
            method:"DELETE"
        })

        window.location.reload()
    }

    return(
        <div className = 'image-card'>
            <img className = 'image-img' src = {image} alt = {id}/>
            <button className="delete_game" onClick={() => handleDelete(image.id)}>Delete</button>
        </div>
    )
}
export default Image