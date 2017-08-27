$(window).ready(function () {
    (function ($) {
        $(function () {
            $('#back-preload').fadeOut(500);
            $('body').css({'overflow': 'visible'});
            $(".button-collapse").sideNav();
            $('.parallax').parallax();
            $('.scrollspy').scrollSpy({scrollOffset: 64});
            var mediaquery = window.matchMedia("(max-width: 600px)");
            if (mediaquery.matches) {
                $('.cabecera.slider').slider({
                    height: 450, indicators: false, interval: 10000
                });
            } else {
                $('.cabecera.slider').slider({
                    height: 600, indicators: true, interval: 10000
                });
            }
            $('.carousel.carousel-slider').carousel({fullWidth: true});

        });
    })(jQuery);
});

