import React, {useState} from 'react';
import SignupForm from './SignUp';


function Login({setLogin, setSignUp}){
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    

    console.log(password)
    console.log(username)
    const handleLogin = (e) => {
    e.preventDefault()
    fetch('/login',{
       method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({username, password})
    })
    .then(res => res.json())
    .then(user => { setLogin(user)})  //set user in state
    }
    if(setLogin){
    return (
        <form onSubmit={handleLogin}>
            <label>
                Username:
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    />
            </label>
            <br />
            <label>
                Password:
                <input
                    type='password'
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    />
            </label>
            <br />
            <button type='submit'>Log In</button>
        </form>
    )
    }else{
    return(
        <div>
         <button type='signup' setSignUp={setSignUp} >Signup</button>
         <SignupForm/>
        </div>
 )}
}   

export default Login