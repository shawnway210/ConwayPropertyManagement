import React from "react";


function Image({images, image, id, setImages}){
console.log(image)
    function handleDelete(id){
    
        fetch(`/images/${id}`,{
            method:"DELETE"
        })
        .then(()=> {
            const filteredImages = images.filter(image =>{
            console.log(image)
            console.log(id)
            return (image.id !== id)
        })
        setImages(filteredImages)
        console.log(filteredImages)
        })
    
        
    }    

    return(
        <div className = 'image-card'>
            <img className = 'image-img' src = {image} alt = {id}/>
            <button className="delete_image" onClick={() => handleDelete(id)}>Delete</button>
        </div>
    )
}
export default Image