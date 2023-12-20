$(document).ready(function(){
  $("#botao").click(function(){
    $.ajax({
      url: "/botao?timestamp=" + new Date().getTime(),
      type:"POST",
      success:function(response){
        window.location.href= "/formulario";
        $("#chamada").text(response.message);
      },
      error: function(){
        console.log(error);
      }
    });
  });
});