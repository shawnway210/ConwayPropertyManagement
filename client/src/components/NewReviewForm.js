import react from 'react';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';


function NewReviewForm(setReviews){
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [rating, setRating] = useState("");
    const [comment, setComment] = useState("");
    const [property, setProperty] = useState("");
    const history = useHistory

    const handleSubmit = (e) => {
        e.preventDefault()

        const gameForm = {
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
                image
            }),
        }

        fetch('http://127.0.0.1:5555/reviews', gameForm)
    }
    return
}
export default NewReviewForm