'use strict';

let numbers = [];

while (true) {
    const num = parseInt(prompt('Please input a number'));
    if (isNaN(num)) {
        continue
    } else if (!numbers.includes(num)) {
        numbers.push(num);

    } else {
        console.log('This number has been previously given');
        break;
    }
}

numbers.sort(function (a, b) { return a-b; });

console.log(numbers.join());
