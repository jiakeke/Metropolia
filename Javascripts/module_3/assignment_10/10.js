'use strict';

const form = document.querySelector('form');
form.addEventListener(
    'submit',
    function() {
        const firstname = document.querySelector("input[name='firstname']").value;
        const lastname = document.querySelector("input[name='lastname']").value;
        document.querySelector('#target').innerHTML = `Your name is ${firstname} ${lastname }`;
        event.preventDefault();
    }
);

