
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.
//                  v
const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.
//                v
const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.



// for loop through a string
// check the index
// if it is an open ( add to count_open, if cosed ) add to count_close
// check within the loop if the count_close is > count_open, if yes, return false
// if, outside of the for loop, count_open does not equal count_closed, false
// else, return true

function parens(str):
    var count_open = 0
    var count_closed = 0
    for(var i = 0; i > str.length; i++){
        if (str[i] == "("){
            count_open++;
        }
        else if(str[i]==")"){
            count_closed++
        }

        if(count_open<count_closed){
            return false
        }
    }
    if(count_open==count_closed){
        return true
    }
    else{
        return false
    }

