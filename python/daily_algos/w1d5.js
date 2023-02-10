function isPal(str) {
    for(var left=0; left<str.length/2; left++) {
        var right = str.length-1-left;
        if(str[left] != str[right]) {
            return "False";
        }
    }
    return "True";
}

var result1 = isPal("axa");
console.log(result1);

/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */
// level
// racecar
// tacocat

const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

/**
 * Determines if the given str is a palindrome (same forwards and backwards).
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given str is a palindrome or not.
 */
function isPalindrome(str) { }
@cohort-JohnM 

zipArrayIntoMap

/* 
  Zip Arrays into Map
  Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
  Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
};

const keys2 = [];
const vals2 = [];
const expected2 = {};

const keys3 = ['name', 'number', 'type', 'evolves_from']
const vals = ['Gyarados', 130, 'water/flying', 'Magikarp']
const expected3 = {
    name: 'Gyarados',
    number: 130,
    type: 'water/flying',
    evolves_from: 'Magikarp'
}
// RIOT



/**
 * Converts the given arrays of keys and values into an object.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} keys
 * @param {Array<any>} values
 * @returns {Object} The object with the given keys and values.
 */
function zipArraysIntoMap(keys, values) { }