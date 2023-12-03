'use strict';

document.querySelector('form').addEventListener(
    'submit',
    async function(evt) {
        evt.preventDefault();
        let qs = document.querySelector('#query').value;
        let url = `https://api.chucknorris.io/jokes/search?query=${qs}`;
        let response = await fetch(url);
        let json_data = await response.json();
        console.log(json_data);
        let result = document.querySelector('#result');
        for (let item of json_data.result) {
            let article = document.createElement('article');
            let p_tag = document.createElement('p');
            p_tag.innerHTML = item.value;
            article.appendChild(p_tag);
            result.appendChild(article);
        }
    }
);
