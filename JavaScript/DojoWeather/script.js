
function c2f(temp){
    return Math.round(9/5 * temp + 32);
}

function f2c(temp){
    return Math.round(5/9 * (temp - 32));
}

function convert(element){
    console.log(element.value);
    for(var i=1; i<9; i++){
        var tempSpan = document.querySelector("#temp" + i);
        var tempVal = parseInt(tempSpan.innerHTML);
        if(element.value == "C"){
            tempSpan.innerText = f2c(tempVal);
        }else{
            tempSpan.innerText = c2f(tempVal);
        }
    }
}

function popup(){
    alert("Loading weather report...");
    console.log("alert");
}

function remove(element){
    document.querySelector(element).remove(".cookie");
    console.log("removed");
}
