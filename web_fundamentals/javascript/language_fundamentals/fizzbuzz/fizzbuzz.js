function fizzbuzz(count){
    for(var i=1;i<=100; i++){
        if( count % 3 == 0 && count % 5 != 0){
            console.log("Fizz");
        } else if( count % 5 == 0 && count % 3 != 0){
            console.log("Buzz");
        } else if(count % 3 == 0 && count % 5 == 0){
            console.log("FizzBuzz");
        } else if (count % 3 != 0 || count % 5 != 0){
            console.log(count);}
        count++;
}
        }

console.log(fizzbuzz(1));