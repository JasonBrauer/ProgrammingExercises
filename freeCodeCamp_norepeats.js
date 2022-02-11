// 24 - (2! * (4-2+1) + 2! * (4-2+1))
// = 24 - (4 + 4) = 16

// 6 - (2! * (3-2+1) + 0)) = 4

function permAlone(str) {
    let countStringInstances = _countEachChar(str);
    let permutationCountObj = _countOfRepeatPermutations(str, countStringInstances);

    console.log(countStringInstances, permutationCountObj);

    let totalRepeatPermutations = 0
    for (let key of Object.keys(permutationCountObj)) {
        totalRepeatPermutations += permutationCountObj[key];
    }

    return _factorial(str.length) - totalRepeatPermutations;
}


function _countEachChar(inputString) {
    // counts and returns the number of instances for each character
    let countStringInstances = {};

    for (let charCheck of inputString) {
        let charCount = 0;
        
        for (let charCompare of inputString) {
            (charCheck == charCompare) ? charCount++ : charCount
        }
        inputString.replace(charCheck, '');
        countStringInstances[charCheck] = charCount;
    }

    return countStringInstances;
}


function _countOfRepeatPermutations(inputString, charCountObj) {
    // calculates the number of permutations possible where each characters could be repeated
    // count(repeats for char considering)! - (total number of characters - count(char considering))
    // where (total number of characters - count(char considering) + 1) = number possible positions where repeating
    let permutationCountObj = {};


    for (let key of Object.keys(charCountObj)) {
        permutationCountObj[key] = (
            // if count of a character is 1, it can't have multiple permutations, so set to 0 
            (charCountObj[key] == 1) ? 0 : _factorial(charCountObj[key]) * 
            (inputString.length - charCountObj[key] + 1)
        )
    }
    
    return permutationCountObj;
}


function _factorial(positiveInteger) {
    let factorial = 1;

    for (let val of _range(1, positiveInteger)) {
        factorial = factorial * val;
    }
    
    return factorial;
}


function _range(start, end) {
    let range = [];

    for (let i=start; i<=end; i++) {
        range.push(i);
    }

    return range
}


console.log(permAlone('aab'));