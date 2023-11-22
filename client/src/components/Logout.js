import React from "react";

function NavBar({setLogout}){
    function handleLogout(){
        fetch("/logout", {
            method: "DELETE",
        }).then(() => setLogout())
    }
    return(
        <header>
            <button onClick={handleLogout}/>
        </header>
    )
}
export default Logout