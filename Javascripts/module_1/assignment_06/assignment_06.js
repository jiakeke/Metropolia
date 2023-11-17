'use strict';

let num, todo, root;
todo = confirm("Should I calculate the square root?");

if (todo == true) {
    num = prompt("Please input a number: ");
    if (isNaN(Number(num, 10))) {
        document.querySelector('#result').innerHTML = `Please input a valid number.`;
    } else {
        num = parseFloat(num);
        if (num < 0) {
            document.querySelector('#result').innerHTML = 'The square root of a negative number is not defined.';
        } else {
            root = Math.sqrt(num);
            document.querySelector('#result').innerHTML = `The square root of ${num} is ${root}`;
        }
    }
} else {
    document.querySelector('#result').innerHTML = 'The square root is not calculated.';
}
