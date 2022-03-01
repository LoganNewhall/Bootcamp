var liked = 0;

function add(){
    console.log("liked");
    console.log(liked);
    liked++;
    document.querySelector("#counter").innerHTML = liked + " like(s)";
}
