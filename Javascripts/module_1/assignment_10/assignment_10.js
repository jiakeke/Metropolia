'use strict';

function randInt(min, max) {
    return Math.floor(Math.random()*(max-min))+min
}

let num, eye_sum, times, sum, prob;
num = parseInt(prompt("Please input a number of dice: "));
eye_sum = parseInt(prompt("Please input the expected sum of dice: "));
times = 0

for (let i=0; i<10000; i++) {
    sum = 0;
    for (let j=0; j<num; j++) {
        let tmp = randInt(1, 7);
        sum += tmp;
    }
    if (sum == eye_sum) {
        times ++;
    }
}


prob = (100*times/10000).toFixed(2);
document.querySelector('#result').innerHTML = 
    `Probability to get sum ${eye_sum} with ${num} dice is ${prob}%`;
