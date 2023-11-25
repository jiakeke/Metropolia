'use strict';

function randInt(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
}

function even(array) {
    let res = [];
    for (const v of array) {
        if (v%2==0) {
            res.push(v);
        }
    }
    return res;
}

let array1 = [];

for (let i=0; i<10; i++) {
    array1[i] = randInt(0, 10);
}


let array2 = even(array1);

console.log(array1);
console.log(array2);
