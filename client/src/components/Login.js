import React, {useState} from 'react';

function Login(){
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const handleLogin = (e) => {
        e.preventDefault()
    }

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
}
export default Login