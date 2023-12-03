'use strict';

async function fetch_random_joke() {
    let joke_data = await fetch('https://api.chucknorris.io/jokes/random');
    let json_data = await joke_data.json();
    console.log(json_data.value);
}
fetch_random_joke();
