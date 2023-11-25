'use strict';

let names = [];
let num = parseInt(prompt('Please input the number of participants.'));

for (let i=0; i<num; i++) {
    names[i] = prompt(`Please input the name of No. ${i+1}`)
}
names.sort();

let tmp = '<ol>\n'
for (let i=0; i<num; i++) {
    tmp += `    <li>${names[i]}</li>`;
}

tmp += '</ol>'

document.querySelector('#result').innerHTML = tmp;
