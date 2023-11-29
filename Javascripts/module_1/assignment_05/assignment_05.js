'use strict';

let year, year_type;
year = parseInt(prompt("Please input a year"));

if (year == 0) {
    year_type = ' not ';
} else if (year % 400 == 0){
    year_type = '';
} else if (year % 4 == 0 && year % 100 != 0) {
    year_type = '';
} else {
    year_type = ' not ';
}

document.querySelector('#result').innerHTML = `${year} is ${year_type}a leap year.`;
