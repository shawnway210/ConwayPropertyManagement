import React from "react";

function Logout({setLogout}){
    function handleLogout(){
        fetch("/logout", {
            method: "DELETE",
        }).then(() => setLogout())
    }
    return(
        <header>
            <button onClick={handleLogout} type="button">Logout</button>
        </header>
    )
}
export default Logout