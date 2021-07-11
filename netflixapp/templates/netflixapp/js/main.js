document.addEventListener("DOMContentLoaded", () => {
    const elementosCarousel = document.querySelectorAll('.carousel');
    M.Carousel.init(elementosCarousel, {
        duration: 250,
        dist: -60,
        shift: 20,
        padding: 35,
        numVisible: 5,
        indicators: true,
        noWarp: false
    });
});