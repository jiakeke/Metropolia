'use strict';

document.querySelector('#start').addEventListener(
    'click',
    function() {
        const operations = [
            { operator: '+', method: function(a, b) {return a+b}},
            { operator: '*', method: function(a, b) {return a*b}},
            { operator: '/', method: function(a, b) {return a/b}},
            { operator: '-', method: function(a, b) {return a-b}},
        ];
        const result = document.querySelector('#result');
        let calculation = document.querySelector('#calculation').value;
        for (let item of operations) {
            if (calculation.includes(item.operator)) {
                const operator = item.operator;
                const method = item.method;
                const cal_array = calculation.split(operator);
                const num1 = parseInt(cal_array[0]);
                const num2 = parseInt(cal_array[1]);
                if (num2 == 0 & operator == '/') {
                    result.innerHTML = '"0" cannot be used as a divisor.'; 
                } else {
                    let res = method(num1, num2);
                    result.innerHTML = res; 
                }
                break;
            }
        }

    }
)
