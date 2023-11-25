'use strict';

function concat(array) {
    let tmp = '';
    for (const v of array) {
        tmp += v;
    }
    return tmp
}

let array = ['White', 'Black', 'Red', 'Yellow', 'Blue'];

document.querySelector('#result').innerHTML = concat(array);
