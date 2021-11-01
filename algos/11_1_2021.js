// Zip Arrays into Map
// Given two arrays, create an associative array (aka hash map, an obj/dictionary) containing keys from the first array, and values from the second.
const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
  abc: 42,
  3: "wassup",
  yo: true,
};

const keys2 = ["abc", 3, "yo", "bro"];
const vals2 = [42, "wassup", true];
const expected2 = {
  abc: 42,
  3: "wassup",
  yo: true,
  bro: null
};

const keys3 = ["abc", 3, "yo"];
const vals3 = [42, "wassup", true, 'bro'];
const expected3 = {
  abc: 42,
  3: "wassup",
  yo: true,
  "?":"?"
};

function zipArraysIntoMap(keys,values){
    if (values.length > keys.length){
        return false
    }
    var dict = {}
    for (i = 0; i < keys.length; i++){
        if(values[i] === undefined){
            dict[keys[i]] = null;
        } else{
            dict[keys[i]] = values[i]
        }
    }
    return dict
}
console.log(zipArraysIntoMap(keys3,vals3))

// Invert Hash
// Given an object/dict,
// return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys

const obj1 = { name: "Zaphod", charm: "high", morals: "dicey", strengths:"fighting" };
const expected1 = { Zaphod: "name", high: "charm", dicey: "morals"}

function invertObj(obj){
    var invertedDictionary = {}
    for (const [key, value] of Object.entries(obj)) {
        invertedDictionary[value] = key;
    }
    console.log(invertedDictionary);
}
invertObj(obj1)
