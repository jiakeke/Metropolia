'use strict';

let numbers = [];
while (true) {
    const num = parseInt(prompt('Please input a number, enter 0 to exit.'));
    if (num == 0) {
        break
    }
    numbers.push(num);
}

console.log(numbers);

numbers.sort(function (a, b) {  return b - a;  });

console.log(numbers.join());
