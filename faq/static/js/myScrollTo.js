$(document).ready(function(){
    console.log('recognize me!');
    $('.btn-how-start').on("click", function(){
        console.log('yo');
        $('html, body').animate({scrollTop: $("#faq").offset().top}, 2000);
    });
}());