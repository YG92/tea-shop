function showModal(clicked_id){
  var clickedElement = document.getElementById(clicked_id);
  var close = clickedElement.getElementsByClassName('close')[0];
  var modal = clickedElement.getElementsByClassName('product_detail')[0];
  modal.style.display = "block";

  close.onclick = function(){
    modal.style.display = "none";
  }
}
