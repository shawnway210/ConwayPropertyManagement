import React from "react";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";

function NavBar({ setLogout }){
    function handleLogout(){
        fetch("/logout", {
            method: "DELETE",
        }).then(() => setLogout())
    }

    return (
        <div>
            <header>
                <NavLink to="/signup">Signup</NavLink>
                <NavLink to="/login">Login</NavLink>
                <button onClick={handleLogout}>Logout</button>
                <NavLink to="/properties">Properties</NavLink>
                <NavLink to="/newproperty">Add a Property</NavLink>  
            </header>
        </div> 

        
    )
}
export default NavBar