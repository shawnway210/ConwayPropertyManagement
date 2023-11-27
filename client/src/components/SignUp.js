import React, { useEffect, useState} from "react"
import { useFormik } from "formik"
import * as yup from "yup"

export const SignupForm = (setSignUp) => {
    const [users, setUsers] = useState([{}])
    const [refreshPage, setRefreshPage] = useState(false)
    

    useEffect(() =>{
        console.log("Hey")
        fetch("/users")
            .then(res => res.json())
            .then((data) => {
                setUsers(data)
                
            })
    }, [refreshPage])

    const formSchema = yup.object().shape({
        username: yup.string().required("Invalid Username"),
        password: yup.string().required("Invalid password"),
      });
    console.log(formSchema)
    const formik = useFormik({
        initialValues: {
            username: "",
            password: "",
        },
        validationSchema: formSchema,
        onSubmit: (values, {resetForm}) => {
            fetch("/users", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(values, null, 2),
            }).then((res) => {
                if(res.status === 200) {
                    setRefreshPage(!refreshPage);
                    resetForm()
                console.log(values)
                }
                console.log(values)
            })
        }
    })

   
    return (
        <div>
            <form onSubmit={formik.handleSubmit} setSignUp={setSignUp} style={{margin: "30px"}}>
                <label htmlFor='signup'>SignUp</label>
                <br />
                <br />
                Username:
                <input 
                    id="username"
                    name="username"
                    onChange={formik.handleChange}
                    value={formik.values.username}
                />
                Password
                <input 
                    id="password"
                    name="password"
                    onChange={formik.handleChange}
                    value={formik.values.password}
                />
                <p style={{ color: "red"}}> {formik.errors.username}</p>
                <p style={{ color: "red"}}> {formik.errors.password}</p>
                <button type="submit">Submit</button>
            </form>
            <table style={{ padding: "15px"}}> 
                <tbody>
                    {users.length === 0 ? (
                        <p>Loading</p>
                    ) : (
                        users.map((user, i) => (
                            <>
                                <tr key={i}>
                                    <td>{user.username}</td>
                                    <td>{user.password}</td>
                                </tr>
                            </>
                        ))
                    )}
                </tbody>
            </table> 
        </div>
    )
}
export default SignupForm