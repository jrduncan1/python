// Create a function that, given an array and a delimiter, returns the array as a string with the delimiter separating the values 

function join (arr, seperator) {

    var output = "";

    for (var idx=0; idx < arr.length; idx++) {
        output += arr[idx];
        // console.log(output);
        if (idx != (arr.length-1)) {
            output += seperator;
            // console.log(output);
        }
    }

    console.log(output)
    return output;
}

join([1,3,6,8,9,5,8], " - ")