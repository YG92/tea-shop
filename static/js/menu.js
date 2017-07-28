var menuElem = document.getElementById('menu');
var titleElem = menuElem.querySelector('.menu-icon');

titleElem.onclick = function () {
  menuElem.classList.toggle('open');
};


var navElem = document.getElementById('cats');
var navTitleElem = navElem.querySelector('.touch-cats');

navTitleElem.onclick = function () {
  navElem.classList.toggle('open');
};
