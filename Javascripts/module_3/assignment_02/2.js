'use strict';

const list1 = document.createElement('li');
list1.innerHTML = 'First item';
document.querySelector('#target').appendChild(list1);

const list2 = document.createElement('li');
list2.setAttribute('class', 'my-item');
list2.innerHTML = 'Second item';
document.querySelector('#target').appendChild(list2);

const list3 = document.createElement('li');
list3.innerHTML = 'Third item';
document.querySelector('#target').appendChild(list3);
