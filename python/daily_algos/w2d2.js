/* 
  Given a string,
  return a new string with the duplicates excluded
  //Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";



const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

// 1. Driver 🚗
// 2. Presenter 👩‍💻
// 3. Navigator 🧭
const str2 = "hellooooo";
const expected2 = "helo";


function dedupe(str) {
    var expected = "";
    for (var i = 0; i < str.length; i++) {
        for(var j = 0; j < i; j++){
            if(str[i] == str[j]){
                break;
            }
        }
        if(j==i){
            expected = expected + [str[i]];
        }
    }
    return expected
}

console.log(dedupe(str2))

// create the function and decide what params it needs and what it will return