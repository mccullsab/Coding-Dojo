/* 
  Given a SORTED array of integers, dedupe the array 
  Because array elements are already in order, all duplicate values will be grouped together.
  Ok to use a new array
  Bonus: do it in O(n) time (no nested loops, new array ok)
  Bonus: Do it in-place (no new array)
  Bonus: Do it in-place in O(n) time and no new array
  Bonus: Keep it O(n) time even if it is not sorted
*/

// const nums1 = [1, 1, 1, 1];
// const expected1 = [1];

// const nums2 = [1, 1, 2, 2, 3, 3];
// const expected2 = [1, 2, 3];

const nums3 = [1, 1, 2, 3, 3, 4];
// const expected3 = [1, 3];

// [1,2,3,4]
// []

//create new empty array
// loop throught the array, if the current equals one after, move to the one after, if end result equal to the orginal return original

function dedupe(arr){
    arrnew = [];
    for(var i =0; i<arr.length;i++){
        if (arr[i]!=arr[i+1] && arr[i]==arr[i-1]){
            arrnew.push(arr[i])
        }
    }
    if(arrnew == arr){
        return arr;
    }
    return arrnew;
}

console.log(dedupe(nums3));

// const nums4 = [1, 1];
// const expected4 = [1];

// 1. Driver 🚗
// 2. Presenter 👩‍💻
// 3. Navigator 🧭

// take 5-8 mins to write the pseudocode here:


// create the function and decide what params it needs and what it will return
/* 
  Given two arrays, interleave them into one new array.
  The arrays may be different lengths. The extra items should be added to the
  back of the new array.
*/

const arrA1 = [1, 2, 3];
const arrB1 = ["a", "b", "c"];
// const expected1 = [1, "a", 2, "b", 3, "c"];

const arrA2 = [1, 3];
const arrB2 = [2, 4, 6, 8];
// const expected2 = [1, 2, 3, 4, 6, 8];

const arrA3 = [1, 3, 5, 7];
const arrB3 = [2, 4];
// const expected3 = [1, 2, 3, 4, 5, 7];

const arrA4 = [];
const arrB4 = [42, 0, 6];
// const expected4 = [42, 0, 6];

function nested(arr1, arr2){
    var expected = []
    var count = 0
    for(var i=0;i<arr1.length + arr2.length;i++){
        if (i<arr1.length){
            expected.push(arr1[i])
        }
        for(var x = count; x<arr2.length;x++){
            expected.push(arr2[x]);
            count++;
            break;
        }
    }
    return expected;
}


console.log(nested(arrA4, arrB4));


// 1. Driver 🚗
// 2. Presenter 👩‍💻
// 3. Navigator 🧭

// take 5-8 mins to write the pseudocode here:


// create the function and decide what params it needs and what it will return