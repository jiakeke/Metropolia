'use strict';

document.querySelector('form').addEventListener(
    'submit',
    async function(event) {
        event.preventDefault();
        let query_string = document.querySelector("input[name='q']").value;
        const url = `https://api.tvmaze.com/search/shows?q=${query_string}`
        try {
            let response = await fetch(url);
            let json_data = await response.json();
            console.log(json_data);
        } catch (error) {
            console.log(error.message);
        } finally {
            console.log('Asynchronous load complete');
        }

    }
);
