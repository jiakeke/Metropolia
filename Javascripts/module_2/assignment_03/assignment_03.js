'use strict';

let names = [];
let num = 6;

for (let i=0; i<num; i++) {
    names[i] = prompt(`Please input the name of No. ${i+1} dog.`)
}
names.sort();
names.reverse();

let tmp = '<ul>\n'
for (let i=0; i<num; i++) {
    tmp += `    <li>${names[i]}</li>`;
}

tmp += '</ul>'

document.querySelector('#result').innerHTML = tmp;
