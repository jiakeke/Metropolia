'use strict';


function randInt(min, max) {
    return Math.floor(Math.random()*(max-min))+min
}

let num, room, msg;

name = prompt('Please input your name');

num = randInt(1, 5);
switch (num) {
    case 1:
        room = 'Gryffindor';
        break;
    case 2:
        room = 'Slytherin';
        break;
    case 3:
        room = 'Hufflepuff';
        break;
    case 4:
        room = 'Ravenclaw';
}

msg = `${name}, you are ${room}.`;
document.querySelector('#msg').innerHTML = msg;
