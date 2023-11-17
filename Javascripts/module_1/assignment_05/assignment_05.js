'use strict';

let year, year_type;
year = parseInt(prompt("Please a year"));

if (year % 400 == 0){
    year_type = 'leap';
} else if (year % 4 == 0 & year % 100 != 0) {
    year_type = 'leap';
} else {
    year_type = 'common';
}

document.querySelector('#result').innerHTML = `${year} is a ${year_type} year.`;
