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
            const result = document.querySelector('#results');
            const fake_img =
                'https://via.placeholder.com/210x295?text=Not%20Found';
            result.innerHTML = '';
            for (let item of json_data) {
                let article = document.createElement('article');
                article.setAttribute('class', 'show');
                result.appendChild(article);

                let head2 = document.createElement('h2');
                head2.innerHTML = item.show.name;
                article.appendChild(head2);

                let link = document.createElement('a');
                link.setAttribute('href', item.show.url);
                link.setAttribute('target', '_blank');
                link.innerHTML = item.show.url;
                article.appendChild(link);

                let new_line = document.createElement('br');
                article.appendChild(new_line);
                let img = document.createElement('img');
                img.setAttribute('src', fake_img);
                if (item.show.image) {
                    img.setAttribute('src', item.show.image.medium);
                }

                img.setAttribute('alt', item.show.name);

                let link_img = document.createElement('a');
                link_img.setAttribute('href', item.show.url);
                link_img.setAttribute('target', '_blank');

                link_img.append(img);
                article.appendChild(link_img);

                let summary = document.createElement('div');
                summary.innerHTML = item.show.summary;
                article.appendChild(summary);
            }
        } catch (error) {
            console.log(error.message);
        } finally {
            console.log('Asynchronous load complete');
        }

    }
);
