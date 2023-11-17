import react from "react";


function Image({image, id}){

    return(
        <img className = 'image-img' src = {image} alt = {id}/>
    )
}
export default Image