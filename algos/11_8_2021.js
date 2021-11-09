/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

const str2 = "   hello  world my friend is tyler     ";
const expected2 = "hello  world my friend is tyler";

function trim(str){
    var trimmedStr = ""
    for(let i = 0; i < str.length; i++){
        if(str[i] === " " && str[i+1] === " "){
            continue
        }
        trimmedStr += str[i]
    }
    return trimmedStr.slice(1, trimmedStr.length - 1)
}

console.log(trim(str2))

//*******************//