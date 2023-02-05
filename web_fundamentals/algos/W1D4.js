var x = 5;

// declare you are making a function then give it a name that describes its purpose
// functions are are asynchronous - they run the code (execute) only when called on.
//functions listen until they are invoked (or called)

function setX(newValue) {
    x=newValue;
}

console.log(x);
//log 5
setX(15);
console.log(x);
//log15

// -------------------//

//amount is a parameter
var x = 5;
    
function addToX(amount) {
    return x + amount;
    console.log("hello there");
}
    
console.log(x);
    //output: 5
var result = addToX(-10);
console.log(result);
    //result = -5 (no hello there because anytime we use a return our function ends there it stops)
    //the function gives back whatever is after the return
console.log(x);
    //output: 5

// -------------------//

//we get values out of an array with index - fetch the value from an array this way

function isPal(arr) {
    for(var left=0; left<arr.length/2; left++) {
        var right = arr.length-1-left;
        if(arr[left] != arr[right]) {
            return "Not a pal-indrome!";
        }
    }
    return "Pal-indrome!";
}
    
var result1 = isPal( [1, 1, 2, 2, 1] );
console.log(result1);
// not a palindrome!

var result2 = isPal( [3, 2, 1, 1, 2, 3] );
console.log(result2);
// palindrome!