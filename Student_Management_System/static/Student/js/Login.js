var x = document.getElementById("password")

function show_password(){
    if(x.type == "text"){
        x.type = "password"
    }
    else{
        x.type = "text"
    }
}