var arr2d = [[2, 5, 8],
[3, 6, 1],
[5, 7, 7]];

// We can console.log the `8` in this array if we
console.log(arr2d[0][2]);
// the first index `0` will select the `[2, 5, 8]` sub-array
// the second index `2` will select the `8` out of that sub-array

for (var row = 0; row < arr2d.length; row++) {
    console.log(arr2d[row]);
    for (var col = 0; col < arr2d[row].length; col++) {
        console.log(arr2d[row][col]);
    }
}

// Write a function called isPresent2d(arr2d, value) that returns true if the value is present and false otherwise
// Note - Don't assume the array will always be the same size, we must rely on its .length property
// Hint - Can we put a for loop inside another for loop?

var arr2d = 
[[2, 5, 8],
[3, 6, 1],
[5, 7, 7]];

function isPresent2d(arr2d, value) {
    for (var row = 0; row < arr2d.length; row++) {
        // console.log(arr2d[row]);
        for (var col = 0; col < arr2d[row].length; col++) {
            // console.log(arr2d[row][col]);
            if (value == arr2d[row][col]){
                console.log("true")
                return true
            }
        }
    }
    console.log("false")
}

isPresent2d(arr2d, 8);

// complete the following function
function flatten(arr2d) {
    var flat = [];
    for (var row = 0; row < arr2d.length; row++) {
        for (var col = 0; col < arr2d[row].length; col++) {
            flat.push(arr2d[row][col])
}
    }
    return flat;

}

var result = flatten([[2, 5, 8], [3, 6, 1], [5, 7, 7]]);
console.log(result); // we expect to get back [2, 5, 8, 3, 6, 1, 5, 7, 7]