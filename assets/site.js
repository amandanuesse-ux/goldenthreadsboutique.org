// Mobile menu
(function(){
  var b=document.querySelector('.menu-toggle'),n=document.getElementById('nav');
  if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});}
})();
// Request form: show the fields for the chosen path
(function(){
  var f=document.getElementById('request-form');if(!f)return;
  function update(){
    var v=f.querySelector('input[name="Request type"]:checked').value;
    var path=v.indexOf('Staff')===0?'staff':'refer';
    f.querySelectorAll('.path').forEach(function(el){
      var on=el.getAttribute('data-path')===path;
      el.hidden=!on;
      el.querySelectorAll('input,select,textarea').forEach(function(i){i.disabled=!on});
    });
    document.getElementById('submit-btn').textContent=path==='staff'?'Send request':'Send recommendation';
  }
  f.querySelectorAll('input[name="Request type"]').forEach(function(r){r.addEventListener('change',update)});
  update();
})();
