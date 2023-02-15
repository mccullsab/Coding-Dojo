// /* 
// Given a non-empty array of odd length containing ints where every int but one
// has a matching pair (another int that is the same)
// return the only int that has no matching pair.
// */

// const nums1 = [1];
// const expected1 = 1;

// const nums2 = [5, 4, 5];
// const expected2 = 4;

// //                                v
// const nums3 = [5, 4, 3, 4, 3, 4, 5];
// const expected3 = 4; // there is a pair of 4s but one 4 has no pair.

// const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
// const expected4 = 1;

// var arr = ["userconfig", "general", "name"];
// var dataStructure = arr.reduceRight(function (value, key) {
//     var obj = {};
//     obj[key] = value;
//     return obj;
// }, 'myVal');

// function frequency(arr) {
//     var expected = {};
//     for (var i = 0; i < arr.length; i++) {
//         if (arr[i] in output) {
//             output[arr[i]]++;
//         }
//         else {
//             output[arr[i]] = 1;
//         }
//     }
//     return expected
// }


const arr1 = ["a", "a", "a"];
// const expected1 = {
//   a: 3,
// };

const arr2 = ["a", "b", "a", "c", "Bob", "c", "c", "d"];
// const expected2 = {
//   a: 2,
//   b: 1,
//   c: 3,
//   Bob: 1,
//   d: 1,
// };

const arr3 = [];
// const expected3 = {};


function frequency(arr) {
    var expected = {};
    for (var i = 0; i < arr.length; i++) {
        if (expected.hasOwnProperty(arr[i])) {
            expected[arr[i]]++;
        }
        else {
            expected[arr[i]] = 1;
        }
    }
    return expected
}

console.log(frequency(arr1))


// loop through the array
//put dict key into empty dict if does not exist and set equal to 1
// add one to key if it already exists


// create the function and decide what params it needs and what it will return




function frequency(arr) {
    var expected = {};
    for (var i = 0; i < arr.length; i++) {
        if (expected.hasOwnProperty(arr[i])) {
            expected[arr[i]]++;
        }
        else {
            expected[arr[i]] = 1;
        }
    }
    return expected
}
ADD for (var key in expected){
    if(newDict[key] % 2 ==1){
        return key
    }
}

//loop over an inject for **key in **object
//loop over an array for X of array