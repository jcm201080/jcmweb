$(document).ready(function(){
    //Efecto Menu
    $('.menu a').each(function(index,elemento){
        $(this).css({
            'top':'-200px'
        });

        $(this).animate({
            top: '0'
        },2000+(index * 500));
    });


    if($(window).width()>800){
        $('header .texto').css({
            opacity: 0, 
            marginTop: 0
        });

        $('header .texto').animate({
            opacity: 1, 
            marginTop: '-52px'
        }, 1500);

    }

    //scrol Elementos Menu
    var acercaDe = $('#acerca-de').offset().top,
        trabajo = $('#trabajos').offset().top,
        contacto = $('#contacto').offset().top;


    $('#btn-acerca-de').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({
            scrollTop: acercaDe 
        }, 500);
    });

    $('#btn-trabajos').on('click', function(e){
		e.preventDefault();
		$('html, body').animate({
			scrollTop: trabajo 
		},500);
	});
    $('#btn-contacto').on('click', function(e){
		e.preventDefault();
		$('html, body').animate({
			scrollTop: contacto 
		},500);
	});
   

});