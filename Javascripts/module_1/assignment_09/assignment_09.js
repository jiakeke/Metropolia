'use strict';


function check_prime(num) {
    for (let i=2; i<=num/2; i++) {
        if (num%i==0) {
            return 'composite';
        }
    }
    return 'prime';
}

let msg;
let num = parseInt(prompt('Please input a integer number:'));
if (num<2) {
    msg = `The number ${num} is neither prime nor composite.`;
} else {
    msg = `The number ${num} is a ${check_prime(num)} number.`;
}
document.querySelector('#result').innerHTML = msg;
    
