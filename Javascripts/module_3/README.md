## Module 3. BOM, DOM and events
[Download this ZIP-file](https://github.com/ilkkamtk/module3-starters), extract it and move the content to the folder where you have your other files for this course.
1. Open `t1` folder in your IDE/editor. Add HTML by using innerHTML property (**2p**)
   - Add the following HTML code to the element with `id="target"`
   ```html
   <li>First item</li>
   <li>Second item</li>
   <li>Third item</li>
   ```
   - Add class `my-list` to the element with `id="target"`
   - [Check assignment](https://js-checker.azurewebsites.net/#/student/64524f3e9e9d273d01b2c867)
2. Open `t2` folder in your IDE/editor. Add HTML by using `createElement()` and `appenChild` mehtods. (**2p**)
   - Add the following HTML code to the element with `id="target"`
   ```html
   <li>First item</li>
   <li>Second item</li>
   <li>Third item</li>
   ```
   - Add class `my-item` to the second list item
   - [Check assignment](https://js-checker.azurewebsites.net/#/student/64524f3e9e9d273d01b2c86d)
3. Open `t3` folder in your IDE/editor. Add HTML by using innerHTML property. (**2p**)
   - Add the following HTML code to the element with `id="target"`. Add the values from 'names' array to the `<li>` elements in a for-loop.
   ```html
   <li>John</li>
   <li>Paul</li>
   <li>Jones</li>
   ```
    - [Check assignment](https://js-checker.azurewebsites.net/#/student/64524f3e9e9d273d01b2c873)
4. Open `t4` folder in your IDE/editor. Add HTML by using `createElement()` and `appenChild` mehtods. (**2p**)
   - Add the following HTML code to the element with `id="target"`. Add the values from 'students' array to the `<option>` elements in a for-loop.
   ```html
   <option value="2345768">John</option>
   <option value="2134657">Paul</option>
   <option value="5423679">Jones</option>
   ```
   - open Element Inspector from DevTools to see the full result. (right click, inspect...)
   - [Check assignment](https://js-checker.azurewebsites.net/#/student/64524f3e9e9d273d01b2c879)
5. Open `t5` folder in your IDE/editor. Create multiple `<article>` elements that contain heading, image, image caption and text and populate them with the data from `picArray`. Add the articles to the `<section>` element. (**5p**)
   - The structure of the articles should be this:
   ```html
   <article class="card">
      <h2>title_from_picArray</h2>
      <figure>
         <img src="medium_image_from_picArray" alt="title_from_picArray">
         <figcaption>caption_from_picarray</figcaption>
      </figure>
      <p>description_from_picArray</p>
   </article>
   ```
    - [Check assignment](https://js-checker.azurewebsites.net/#/student/64524f3e9e9d273d01b2c87f)
6. Open `t6` folder in your IDE/editor. Make a script that opens an alert window that says 'Button Clicked' when the `<button>` element is clicked. (**1p**)
7. Open `t7` folder in your IDE/editor. Make a hover effect with JavaScript. (**2p**)
   - when user mouses over `<p id="trigger">` change the picture of `<img id="target">` form `picA.jpg` to `picB.jpg`
   - when user mouses off, change the picture back to original
   - [Check assignment](https://js-checker.azurewebsites.net/#/student/64524f3e9e9d273d01b2c88b)
8. Open `t8` folder in your IDE/editor. Make a simple calculator. (**4p**)
   - There are two input fields where user enters numbers. Based on the drop-down list, calculator performs addition, subtraction, multiplication or division of these two numbers.
   - Use the value attribute of `<option>` elements to decide which operation the calculator needs to do. [Example.](https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_select_value2)
   - Show the result in `<p id="result">` when the button is clicked.
   - [Check assignment](https://js-checker.azurewebsites.net/#/student/64524f3f9e9d273d01b2c891)
9. Open `t9` folder in your IDE/editor. This is continuation to previous task. There is only one text field left, where the user writes the calculation (addition, subtraction, multiplication or division) (**4p**)
   - You can use the [includes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/includes) and [split](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split) methods.
   - eval() function is prohibited
   - No need to support decimal numbers, calculating integers is enough.
   - Example inputs: `3+5`, `2-78`, `3/6`, etc..
   - [Check assignment](https://js-checker.azurewebsites.net/#/student/64524f3f9e9d273d01b2c897)
10. Open `t10` folder in your IDE/editor. Read the first name and last name values from the form and print them in the `<p id="target">` (**2p**)
    - remember to stop the default action of the form
    - you can use [attribute selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) in querySelector() to select the `<input>` elements
    - example output: `Your name is Luke Skywalker`
    - [Check assignment](https://js-checker.azurewebsites.net/#/student/64524f3f9e9d273d01b2c89d)
11. Continue task 5. Folder `t11` already exists. Follow the instructions in `t11.txt`. Modify the program to open large image in a [modal](#modal) when `<article>` is clicked. (**6p**)
    - kick yourself at this point if you used innerHTML to create the `<article>` and its content.
    - add the following html code between `</div>` and `</body>` manually to the HTML-document (no JS)
    ```html
    <dialog>
       <span>&#x2715;</span>
       <img>
    </dialog>
    ```
    - picArray has two images for each item: medium and large. Medium is used in the `<img>` inside the `<article>` and large is used in the `<img>` inside the `<dialog>`.
    - use [showModal() and close()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement#instance_methods) functions to show and hide `<dialog>`
    - the same time you are opening the modal, you should put the large image to the `<img>` in the modal. 
    - Don't forget to add `alt` attribute.
    - use `<span>` inside `<dialog>` to close the modal.
    - [Check assignment](https://js-checker.azurewebsites.net/#/student/64524f3f9e9d273d01b2c8a3)
<hr>
<sub id="modal"><sup>- A modal is a dialog box/popup window that is displayed on top of the current page</sup></sub>

