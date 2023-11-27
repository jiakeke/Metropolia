'use strict';

let html = '<li>First item</li>\n<li>Second item</li>\n<li>Third item</li>'

document.querySelector('#target').innerHTML = html;
document.querySelector('#target').setAttribute('class', 'my-list');

