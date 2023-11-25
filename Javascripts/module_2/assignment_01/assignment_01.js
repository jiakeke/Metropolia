'use strict';

const numbers = [];
for (let i=0; i<5; i++) {
    numbers[i] = prompt('Please input a number');
}

for (let j=4; j>=0; j--) {
    console.log(numbers[j]);
}
