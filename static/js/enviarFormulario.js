$(document).ready(function () {
    $("#formulario").submit(function (event) {
        var dados = {
            nome: $("#nome").val(),
            idade: $("#idade").val()
        };

        $.ajax({
            url: "/formulario/receber",
            type: "POST",
            contentType: "application/json;charset= UTF-8",
            data: JSON.stringify(dados),
            success: function (response) {
                window.location.href = "/database";
                $("#resultado").text(response.message);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});
