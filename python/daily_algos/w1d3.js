/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

// loop through the array to grab the value
    // convert int to str
// loop through again to inject the seperator
// if the length on the list is less than 2 then we do no add seperator

function join(arr, separator) {
    var expected = ""
    for(var i = 0; i<arr.length; i++){
        if (i < arr.length -1){
            expected += arr[i].toString()
        }
        else{
            expected += arr[i].toString() + separator;
        }
        
    }
    return expected
}

console.log(join(arr4, separator4));


// if(arr.length <= 1){
//     return arr.toString();
// }
// else{
// don't forget to call the function!