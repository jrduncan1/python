/* 
  Given an array of strings
  return a sum to represent how many times each array item is found (a frequency table)
  Useful methods:
    Object.hasOwnProperty("keyName")
      - returns true or false if the object has the key or not
    Python: key in dict
*/

const arr1 = ["a", "a", "a"];
const expected1 = {
  a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

function frequencyTableBuilder(arr) {
    const results = {}
    for(var i = 0; i < arr.length; i++){
        if(results.hasOwnProperty(arr[i])){
            results[arr[i]]++;
        } else{
            results[arr[i]] = 1;
        }
    }
    return results
}
console.log(frequencyTableBuilder(arr2))

