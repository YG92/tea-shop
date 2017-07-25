var modal = document.getElementById('product_detail');
var close = document.getElementById('close');
var trigger = document.getElementById('trigger');


trigger.onclick = function(){
  modal.style.display = "block";
}

close.onclick = function(){
  modal.style.display = "none";
}
