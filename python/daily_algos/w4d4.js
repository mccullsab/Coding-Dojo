/*
  Recursive Binary Search

  Input: SORTED array of ints, int value
  Output: bool representing if value is found

  Recursively search to find if the value exists, do not loop over every element.

  Approach:
  Take the middle item and compare it to the given value.
  Based on that comparison, narrow your search to a particular section of the array
*/

//                   V
const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

//                   V
const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

// don't be afraid to add extra parameters 👇
function binarySearch(sortedNums, searchNum) {

    // base case(s)
    // logic
    // recursive call(s) / return(s)
}

function binarySearch(arr, target, low = 0, high = arr.length -1){
    var mid = Math.floor((low+high)/2)

    
    if(arr.length > 1){
        if(mid == target){
            return true
        } 
        if(mid > target){
            high = mid - 1
            return binarySearch
        }
    }
}