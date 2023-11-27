'use strict';

const p_tag = document.querySelector('#trigger');
const img = document.querySelector('#target');

p_tag.addEventListener(
    "mouseover",
    function(event) {
        img.src = 'img/picB.jpg';
    });

p_tag.addEventListener(
    "mouseout",
    function(event) {
        img.src = 'img/picA.jpg';
    });
