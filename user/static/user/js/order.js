$(function(){
    $('.selectpicker').selectpicker();
});


function hide() {
    $("#roundtrip").hide()
}
function show() {
  $("#roundtrip").show()
}


  (function() {
    'use strict';
    window.addEventListener('load', function() {
      var forms = document.getElementsByClassName('needs-validation');

      var validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
          if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
          }
          form.classList.add('was-validated');
        }, false);
      });
    }, false);
  })();
  $(document).ready(function(){
    $("#arrow1").click(function(){
      $("#arrow1").hide();
      var from = document.getElementById("from");
      var to = document.getElementById("to");
      $("#arrow2"). show();
      t = to.value
      to.value = from.value
      from.value = t
    });
    $("#arrow2").click(function(){
      $("#arrow2").hide();
      $("#arrow1").show();
      f = from.value
      from.value = to.value
      to.value = f

    });
  });