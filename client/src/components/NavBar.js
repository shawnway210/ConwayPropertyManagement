import React from "react";

function NavBar({ setLogout }){
    function handleLogout(){
        fetch("/logout", {
            method: "DELETE",
        }).then(() => setLogout())
    }

    return (
        <header>
            <button onClick={handleLogout}>Logout</button>
        </header>
    )
}
export default NavBar