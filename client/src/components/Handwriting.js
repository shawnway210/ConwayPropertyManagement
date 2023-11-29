import React from "react";
import SignaturePad from "react-signature-pad"

function Handwriting(){
    return(
        <div>
            <h1>Conway Property Management</h1>
            <SignaturePad
            canvasProps={{ className: 'handwriting-canvas'}}
            options={{
                minWidth: 3,
                maxWidth: 3,
                penColor: 'black',
                backgroundColor: 'transparent',
            }}
            />
        </div>
    )
}
export default Handwriting;