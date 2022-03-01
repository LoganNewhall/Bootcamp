function Login(id){
    console.log("Login");
    document.getElementById(id).innerHTML = "Logout";
}

function Definition(element){
    console.log("Definition Added!");
    element.remove();
}

function like(){
    console.log("liked");
    alert("Ninja was liked");
}