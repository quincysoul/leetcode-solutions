
//for the function printFibonnaci, given n, print the sequence including n...
// Time: O(N), SpaceL O(N), no recursion risk of stack overflow.

function printFibonnaci(n)
{
    let first = 0;
    let second = 1;
    let accumulatorArray = [];

    accumulatorArray.push(first);
    if(n === 1)
    {
        return accumulatorArray;
    }

    accumulatorArray.push(second);
    if(n === 2)
    {
        return accumulatorArray;
    }

    for(let i = 3; i < n + 1; i++)
    {
        third = first+second;
        first = second;
        second = third;

        accumulatorArray.push(third);
    }

    return accumulatorArray;
}

let results = printFibonnaci(10);
console.log(results);