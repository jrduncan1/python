/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const two_str1 = "hello";
const two_expected1 = "olleh";

const two_str2 = "hello world";
const two_expected2 = "olleh dlrow";

const two_str3 = "abc def ghi";
const two_expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */

// Using .split .reverse and .join:
function reverseWords(str) {
    return str.split("").reverse().join("").split(" ").reverse().join(" ")
}

console.log(reverseWords(two_str3))

// Using built-out logic:
const two_str1 = "hello";
const two_expected1 = "olleh";

const two_str2 = "hello world";
const two_expected2 = "olleh dlrow";

const two_str3 = "abc def ghi";
const two_expected3 = "cba fed ihg";

function reverseWords(str) {
  var finalString = "";
  var batchReversed = "";
  var batch = "";
  for( let i = 0; i < str.length; i++){
    if( str[i] == " "){
      for( j = batch.length -1; j >= 0; j--){
        batchReversed += batch[j];
      }
      finalString += batchReversed+" ";
      batchReversed = "";
      batch = "";
    }
    else{
      batch += (str[i])
    }
  }
  for( j = batch.length -1; j >= 0; j--){
    batchReversed += batch[j];
  }
  finalString += batchReversed;
  return finalString
}

console.log(reverseWords(two_str1));
console.log(reverseWords(two_str2));
console.log(reverseWords(two_str3));