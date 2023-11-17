'use strict';

function is_leap_year(year) {
    if (year % 400 == 0){
        return true;
    } else if (year % 4 == 0 & year % 100 != 0) {
        return true;
    } else {
        return false;
    }
}

let start, end, result;
result = '<ul>';
start = parseInt(prompt("Please input a start year"));
end = parseInt(prompt("Please input an end year"));

for (let i = start; i <= end; i++) {
    if (is_leap_year(i)) {
        result += `<li>${i}</li>`
    }
}

result += '</ul>';
document.querySelector('#result').innerHTML = result;
