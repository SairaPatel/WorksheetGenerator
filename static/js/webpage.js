function selectAll(){
    // check if "all" checkbox is ticked
    checkbox = document.getElementById("select-all-checkbox");
    if (checkbox.checked){
        // select all number checkboxes
        for (var i = 2; i < 13; i++){
            c = document.getElementById(`checkbox${i}`);
            c.checked = true;
        }
    }
    else{
        // deselect all number checkboxes
        for (var i = 2; i < 13; i++){
            c = document.getElementById(`checkbox${i}`);
            c.checked = false;
        }
    }
}

function validateBoxes(){
    txt = document.getElementById("error-message");

    // check at least 1 box is ticked
    var i = 2;
    while (i < 13){
        c = document.getElementById(`checkbox${i}`);

        // submit form and hide error message

        if (c.checked == true){
            txt.hidden = true;
            return true;
        }
        i++;
    }

    // no boxes ticked so don't submit form. Show error message.
    txt.hidden = false;
    return false;
    
    
}