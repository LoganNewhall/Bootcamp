var num1 = 2;
var num2 = 418;

function changeName(element){
    console.log("name changed");
    document.querySelector(element).innerHTML = "Logan Newhall";
}

function accept(element){
    console.log("accepted");
    removeElement(element);
    num2++;
    document.querySelector(".totalconnections").innerHTML = num2;
}

function deny(element){
    console.log("denied");
    removeElement(element);
}

function removeElement(element){
    num1--;
    document.querySelector(".connect-num").innerHTML = num1;
    document.querySelector(element).remove();
    console.log(num1);
}

