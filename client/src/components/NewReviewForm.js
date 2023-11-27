import React, {useState} from 'react';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';


function NewReviewForm({setReviews}){
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [rating, setRating] = useState("");
    const [comment, setComment] = useState("");
    const [property, setProperty] = useState("");
    const history = useHistory

    const handleSubmit = (e) => {
        e.preventDefault()

    const reviewForm = {
        method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name,
                "property_id": parseInt(property),
                email,
                comment,
                rating: parseInt(rating),
            })
        };

        fetch(`/reviews`, reviewForm)
            .then((res) => res.json())
            .then((data) => {
                setReviews( reviews => [ ...reviews, data ])
                history.push('/reviews')
            })

            setName("");
            setProperty("");
            setEmail("");
            setRating("");
            setComment("");
    }



    return (
        <div className='formContainer'>
            <h3>Please Add A Review</h3>


            <form onSubmit={handleSubmit}>
                <input
                label = 'Name'
                placeholder = 'Name'
                value = {name}
                onChange = {(e) => setName(e.target.value)}
                />
                <input
                    label = 'Email'
                    placeholder = 'Email'
                    value = {email}
                    onChange = {(e) => setEmail(e.target.value)}
                />
                <input
                    label = 'Comment'
                    placeholder = 'Comment'
                    value = {comment}
                    onChange = {(e) => setComment(e.target.value)}
                />
                <input
                    label = 'Property'
                    placeholder = 'Property'
                    value = {property}
                    onChange = {(e) => setProperty(e.target.value)}
                />
                <input
                    label = 'Rating'
                    placeholder='Rating'
                    value = {rating}
                    onChange = {(e) => setRating(e.target.value)}
                    />

                <button className='add_review'>Add Review</button>
            </form>
        </div>   
        
    )
}
export default NewReviewForm