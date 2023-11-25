'use strict';

function roll_dice() {
    // (0, 6]
    return Math.ceil(Math.random()*6)
}

let tmp = '<ul>';

while (true) {
    const res = roll_dice();
    tmp += `    <li>${res}</li>`;
    if (res == 6) {
        break;
    }

}
tmp += '</ul>';
document.querySelector('#result').innerHTML = tmp;
