import React, {useState} from "react";
import { useHistory } from "react-router-dom/cjs/react-router-dom";

function NewImage(setImages){
    const [image, setImage] = useState("")

    const history = useHistory()

    const handleSubmit = (e) => {
        e.preventDefault()

        const newImage = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",    
            },
            body: JSON.stringify({
                image
            })
        }
        fetch("http://127.0.0.1:5555/images", newImage)
            .then((res) => res.json())
            .then((data) => {
                setImages(images => [...images.data])
                history.push('/images')
            })
        setImage("");
    }

    return (
        <div className="formContainer">
            <h3>Add a Photo</h3>

            <form onSubmit={handleSubmit}>
                <input
                    label="Image"
                    placeholder="Image"
                    value={image}
                    onChange={(e) => setImage(e.target.value)}
                    />
                    <button type="submit">Submit</button>
            </form>
            <button className="add_image" onClick={() => handleSubmit(image.id)}>Add a Photo</button>
        </div>
    );
}
export default NewImage