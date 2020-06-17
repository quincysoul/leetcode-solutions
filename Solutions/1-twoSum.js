/*

Being a little rusy on js challenges I took this opportunity to revisit some js things.
js objects which do not allow int as keys, they only allow strings. Can get around this with new Map();
js toString() is too costly for leetcode.
The problem says there is always one solution - but the edge case handling was not what I thought. A target of 0 with two 0 elements is acceptable.

*/

// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.

//Sample : 
// [1,2,3,4,5,0]
// find 6: should return [0,4]
// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.

//Sample : 
// [1,2,3,4,5,0]
// find 6: should return [0,4]
function twoSum(numberArray, targetInt) {

    let sumHashMap = {};

    let i = 0;
    len = numberArray.length;
    for(i; i < len; i++)
    {
        let currentNumInt = numberArray[i];
        console.log("currentNumInt::" + currentNumInt)

        let currentNumStr = currentNumInt.toString();
            let remainderInt = targetInt - currentNumInt;
            let remainderStr = remainderInt.toString();
            console.log("Remainder::" + remainderStr)
            console.log("hasmap at rmstr"+sumHashMap[remainderStr])
            if(sumHashMap[remainderStr] != null) //if hastable has a key == remainder, then I found my two sum.
            {
                console.log("hashmap has rmaint::")
                let otherIndex = sumHashMap[remainderStr]; // indexOfOtherOperand = 
                return [otherIndex,i];
            }
            //else, I need to store my current Number as a hastable key, so others looking for a remainder could find it.
            sumHashMap[currentNumStr] = i
            console.log("hashmap Doesnt have rmaint::" + JSON.stringify(sumHashMap));

        
    }
}
twoSum([2,7,11,15],9);