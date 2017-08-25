$(window).ready(function () {
    window.sr = ScrollReveal({reset: false});
    sr.reveal('.caption-permanent .btn', { duration: 1200, origin: 'bottom' });
    sr.reveal('.quienes-somos .img-item', { duration: 1200, origin: 'left' });
    sr.reveal('.title-section span');
    sr.reveal('.container-servicios .item-servicio', { duration: 1200 }, 100);
});