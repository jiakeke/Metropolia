'use strict';

function randInt(min, max) {
    return Math.floor(Math.random()*(max-min))+min
}

let num
let amount=0;
let detail = '<br><br>Details:<br>';

num = prompt("Please input a number of dice rolls: ");

if ((num == '') || isNaN(Number(num, 10))) {
    document.querySelector('#result').innerHTML = `Please input a valid number.`;
} else {
    num = parseInt(num);
    if (num < 0) {
        document.querySelector('#result').innerHTML = 
            'The number of dice roos needs to be a positive number.';
    } else {
        for (let i = 0; i < num; i++) {
            let tmp = randInt(1, 7);
            amount += tmp;
            detail += `\n ${i+1}. ${tmp}<br>`;
        }
        document.querySelector('#result').innerHTML = 
            `The sum of throwing the dice ${num} times is: ${amount}.${detail}`;
    }
}
