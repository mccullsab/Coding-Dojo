var fruit1 = "apples";
var fruit2 = "oranges";
    
fruit2 = fruit1;
    
console.log(fruit2 + " and " + fruit1);

//apples and apples

var fruit1 = "apples";
var fruit2 = "oranges";
    
var temp = fruit1; // temp is a common name for this
fruit1 = fruit2;
//oranges
fruit2 = temp;
//oranges
    
console.log(fruit2 + " and " + fruit1);

//oranges and oranges

var start = 0;
var end = 12;
    
while(start < end) {
    console.log("start: " + start + ", end: " + end);
    start += 2;
    end -= 2;
}

//start: 0, end: 12
//2, 10 - 4, 8

var arr1 = ["a", "b", "c", "d", "e"];

for(var i=0; i<arr1.length/2; i++){
    
    var temp = arr1[i];
    arr1[i] = arr1[arr1.length - i -1];
    arr1[arr1.length - i -1] = temp
    // arr1[i].push();
    }

console.log(arr1);

//

var arr = ["a", "b", "c", "d", "e"];

var reversed = [];
for (var i = arr.length - 1; i >= 0; i--) {
    reversed.push(arr[i]);
}

console.log(reversed);

//

var arr = ["a", "b", "c", "d", "e"];

for(var i=0; i<arr.length/2; i++){
    temp = arr[i];
    arr[i]=arr[arr.length - 1 - i];
    arr[arr.length - 1 - i] = temp;
}

console.log(arr);