'use strict';

function roll_dice(sides) {
    // (0, sides]
    return Math.ceil(Math.random() * sides);
}

let tmp = '<ul>';

const sides = parseInt(prompt('Please input the number of sides on the dice'));

while (true) {
    const res = roll_dice(sides);
    tmp += `    <li>${res}</li>`;
    if (res == sides) {
        break;
    }

}
tmp += '</ul>';
document.querySelector('#result').innerHTML = tmp;
