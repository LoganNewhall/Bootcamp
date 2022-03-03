console.log("1st Loop!\n");
for(i=1; i<=20; i++){
    if(i % 2 != 0){
        console.log(i);
    }
}

console.log("2nd Loop!\n");
for(i=100; i>=0; i--){
    if(i % 3 == 0){
        console.log(i);
    }
}

console.log("3rd Loop!\n");
for(i=4; i>-4; i-=1.5){
    console.log(i);
}

console.log("4th Loop!\n");
var sum = 0
for(i=1; i<=100; i++){
    sum += i;
}
console.log(sum);

console.log("5th Loop!\n");
var product = 1
for(i=1; i<=12; i++){
    product *= i;
}
console.log(product);
