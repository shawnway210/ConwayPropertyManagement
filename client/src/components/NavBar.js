import React from "react";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";

function NavBar(){
    

    return (
        <div>
            <header>
                <NavLink to="/signup">  Signup  </NavLink>
                <NavLink to="/login">  Login  </NavLink>
                <NavLink to="/logout">  Logout  </NavLink>
                <NavLink to="/properties">  Properties  </NavLink> 
            </header>
        </div> 

        
    )
}
export default NavBar