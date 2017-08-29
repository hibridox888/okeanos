$(window).ready(function () {
    (function ($) {
        $(function () {
            $('ul.tabs').tabs({
                swipeable: true
            });
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
                    height: 450, indicators: true, interval: 10000
                });
            }
            $('.carousel.carousel-slider').carousel({fullWidth: true});

            // Pushpin Demo Init
            if ($('.pushpin-demo-nav').length) {
                $('.pushpin-demo-nav').each(function () {
                    var $this = $(this);
                    var $target = $('#' + $(this).attr('data-target'));
                    $this.pushpin({
                        top: $target.offset().top,
                        bottom: $target.offset().top + $target.outerHeight() - $this.height()
                    });
                });
            }

        });
    })(jQuery);
});

