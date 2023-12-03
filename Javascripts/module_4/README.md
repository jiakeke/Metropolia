## Module 4. AJAX
1. Make an app that retrieves information about a TV series you enter and displays it in the console. (**2p**)
   - API to use: [TVMaze API](http://www.tvmaze.com/api#show-search)
   - First, make a valid HTML page with a search form. Example form:
   ```html
   <form action="https://api.tvmaze.com/search/shows">
     <input id="query" name="q" type="text">
     <input type="submit" value="Search">
   </form>
   ```
   - Test the form. The result should be a page full of JSON formatted data.
2. Develop the app further.
   - Add JavaScript that gets the value entered to the form and sends a request with [fetch](apit-ajax.md#here-is-the-same-example-but-this-time-the-airport-code-is-entered-by-using-a-form) to `https://api.tvmaze.com/search/shows?q=${value_from_input}`. Print the search result to the console. (**3p**)
3. Develop the app even further. Print the following information for all series from the search result on the web page. (**7p**)
   - required information: Name, link to details (url), medium image and summary
   - show the name in `<h2>` element
   - show the url in `<a>` element. Also add `target="_blank"` to the link.
   - show the medium image with `<img src="" alt="">`. Add medium image to `src` attribute and name property to `alt` attribute.
   - some TV-shows don't have images. This will cause an error. You can fix this by adding ? operator to `image` property. Example: `tvShow.show.image?.medium;`. This is called [optional chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining).
   - show summary in `<div>` element (not `<p>`). This is because the summary is already in `<p>` element, and the result will not be valid if `<p>` is inside another `<p>`.
   - collect the elements to `<article>` elements and append `<article>` elements to the HTML document.
      - make `<div id="results">` element to the HTML document where you append the `<article>` elements.  
   - clear the old results with `innerHTML = ''` before you append the new results.
4. Develop the app even further. Optional chaining is not the best way to handle missing image. Use [ternary operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) or if/else to add a default image if TV-show is missing image property. (**2p**)
   - Use `https://via.placeholder.com/210x295?text=Not%20Found` as the default image.
   - [Check assignments 1-4](https://js-checker.azurewebsites.net/#/student/64524f3f9e9d273d01b2c8a9) 
5. Make an app that retrieves a random Chuck Norris joke and displays it in the console. (**2p**)
    - API to use: [chucknorris.io](https://api.chucknorris.io/)
    - Send a request to `https://api.chucknorris.io/jokes/random` and print only the joke to the console (that would be the 'value' property)
    - No need to add a form.
6. Develop the app further (**4p**).
    - Now add a form where you can enter a search term like in assignments 1-3
    - Send the search term to `https://api.chucknorris.io/jokes/search?query=${value_from_input}` using `fetch()`
    - Print each joke in this format:
    ```html
    <article>
        <p>Joke here<p>
    </article>
    ``` 
7. Advanced. Routing with [digitransit](https://digitransit.fi/en/developers/apis/1-routing-api/)  (**16p**)
   - **Not for the faint-hearted**. Don't do this if it interferes with the project. It's not worth it.
   - Create an app that shows the route from user defined address to school (Karaportti 2).
   - You need to have a form where user adds an address. After the form is submitted, the route is displayed on a map. Show also the starting and ending time of the trip. _Not_ each part, just the start and end times.
   - Example: [JS](https://github.com/ilkkamtk/JavaScript-english/blob/main/api-esimerkit/js/esim4.js), [HTML](https://github.com/ilkkamtk/JavaScript-english/blob/main/api-esimerkit/esim4.html)
      - You'll need [this Leaflet plugin](https://github.com/ilkkamtk/JavaScript-english/blob/main/api-esimerkit/js/Polyline.encoded.js) to make the example work.
   - [Here is an example](https://digitransit.fi/en/developers/apis/1-routing-api/itinerary-planning/#basic-route-from-kamppi-helsinki-to-pisa-espoo) on how to use places/addresses with coordinates.
      - To get coordinates from address, you can use [address search ](https://digitransit.fi/en/developers/apis/2-geocoding-api/address-search/)
   - If you get cors errors (which is likely _not_ going to happen) [use this fix](https://github.com/ilkkamtk/corsfix).
