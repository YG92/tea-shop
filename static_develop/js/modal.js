var close = document.getElementById('close');
var modal = document.getElementById('modal');


close.onclick = function(){
  modal.style.display = "none";
}

window.onclick = function(event){
  if(event.target != modal){
    modal.style.display = "none";
  }
}
