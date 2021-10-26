/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

// const str1 = " there's no free lunch - gotta pay yer way. ";
// const expected1 = "TNFL-GPYW";

// const str2 = "Live from New York, it's Saturday Night!";
// const expected2 = "LFNYISN";

// John/Jake/Blair work//

var initialString1 = "Live from New York, it's Saturday Night!"
var initialString2 = " there's no free lunch - gotta pay yer way. "


function acronymize(str){
    var str = str.split(" ")
    var acronym = ""
    if(str[0] === " " && str[str.length - 1] === " "){
        for(i = 1; i < str.length - 1; i++){
            acronym += (str[i][0])
        } 
    }
    else{
        for(i = 0; i < str.length; i++){
            acronym += (str[i][0])
        }
    }
    return acronym
}

console.log(acronymize(initialString1.toUpperCase()))


// Instructor solution //

const str1 = " there's no free lunch - gotta pay yer way. "
const str2 = "Live from New York, it's Saturday Night!"

function acronymize(str){
    var newString = ""

    if(str[0] !== " "){
        char = str[0].toUpperCase()
        newString = char
    }

    for(i = 0; i < str.length - 1; i++){
        if(str[i] === " "){
            char = str[i + 1].toUpperCase()
            newString += char
        }
    }
    return newString
}

console.log(acronymize(str1))
console.log(acronymize(str2))

/*****************************************************************************/

/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const two_str1 = "creature";
const expected1 = "erutaerc";

const two_str2 = "dog";
const expected2 = "god";


function reverseString(str) {
    var newString = ""

    for(i=str.length-1; i>=0; i--){
        newString += str[i]
    }
    return newString
}

console.log(reverseString(two_str1))
console.log(reverseString(two_str2))


/*****************************************************************************/