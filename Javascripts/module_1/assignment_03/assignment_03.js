'use strict';
const num1 = parseInt(prompt('Please input the first integer:'));
const num2 = parseInt(prompt('Please input the second integer:'));
const num3 = parseInt(prompt('Please input the third integer:'));

const sum = `Sum: ${num1}+${num2}+${num3}=${num1+num2+num3}`;
const product = `Product: ${num1}x${num2}x${num3}=${num1*num2*num3}`;
const average = `Average: (${num1}+${num2}+${num3})/3=${(num1+num2+num3)/3}`;

document.querySelector('#sum').innerHTML = sum;
document.querySelector('#product').innerHTML = product;
document.querySelector('#average').innerHTML = average;
