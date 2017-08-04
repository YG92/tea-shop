var images = document.querySelectorAll('.image');
var closeButtons = document.querySelectorAll('.close');

function showModal(clickedElem){
  return function(){
    var parent = clickedElem.parentNode;
    var modal = parent.querySelector('.product_detail');
    modal.style.display = "block";
  }
}

function hideModal(clickedElem){
  return function(){
    var modal = clickedElem.parentNode.parentNode;
    modal.style.display = "none";
  }
}

for (var i = 0; i < images.length; i++) {
  images[i].addEventListener('click', showModal(images[i]));
}

for (var i = 0; i < closeButtons.length; i++) {
  closeButtons[i].addEventListener('click', hideModal(closeButtons[i]));
}
