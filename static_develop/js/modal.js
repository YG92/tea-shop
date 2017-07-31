function showModal(parent){
  var modal = parent.getElementsByClassName('product_detail')[0];
  modal.style.display = "block";
  var close = modal.getElementsByClassName('close')[0];

  close.onclick = function(){
    modal.style.display = "none";
  }
}
