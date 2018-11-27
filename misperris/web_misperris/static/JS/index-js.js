$('header.awSlider .carousel').carousel({
	pause: "hover",
  interval: 2000
});

var startImage = $('header.awSlider .item.active > img').attr('src');
$('header.awSlider').append('<img src="' + startImage + '">');

$('header.awSlider .carousel').on('slid.bs.carousel', function () {
 var bscn = $(this).find('.item.active > img').attr('src');
	$('header.awSlider > img').attr('src',bscn);
});

var r = alert("Registro exitoso");

function Registrosi() {
	var mensaje = confirm("Registrado con exito! Deseas Iniciar Sesion ahora?");
	if (mensaje) {
	$('href="{% url 'login'%}"')
	}
	//Detectamos si el usuario denegó el mensaje
	else {
	$('href="{% url 'index'%}"')
	}
	}
