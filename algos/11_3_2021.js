/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

function parensValid(str) {
    var count = 0
    for(var i = 0; i < str.length; i++){
        if(str[i] === "("){
            count++
        } else if(str[i] === ")"){
            count--
        }
        if(count < 0){
            return false
        }
    }
    return count === 0
}
console.log(parensValid(str1))

// *****************************************************************
