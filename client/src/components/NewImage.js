import React, {useState, useContext} from "react";
import { useHistory } from "react-router-dom/cjs/react-router-dom";
import { DarkModeContext } from "./DarkModeContext";

function NewImage({setImages}){

    const { isDarkMode } = useContext(DarkModeContext)
    console.log(isDarkMode)
    const [image, setImage] = useState("")
    
    const history = useHistory()

    const handleSubmit = (e) => {
        e.preventDefault();

        const newImage = {
            method: "POST",
                headers: {
                "Content-Type": "application/json",    
                },
                body: JSON.stringify({
                    image
                })
            }
            fetch("/images", newImage)
                .then((res) => res.json())
                .then((data) => {
                    setImages(images => [...images,data])
                    history.push('/images')
        })  
        setImage("");
        
    }

    return (
        <div className={isDarkMode ? 'dark' : 'light'}>
            

            <form className='form-card' onSubmit={handleSubmit}>
                <h3>Add a Photo</h3>
                <input
                    label="Image"
                    placeholder="Image"
                    value={image}
                    onChange={(e) => setImage(e.target.value)}
                    />
                <button className="add_image">Add Photo</button>
            </form>
        </div>
    );
}
export default NewImage