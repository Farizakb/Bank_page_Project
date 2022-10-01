$(document).ready(function(){
    $('.slick').slick({
        arrows: true,
        infinite: true,
        slidesToShow: 5,
        slidesToScroll: 1,
        dots: false,
        infinite: true,
        centerMode: true,
        variableWidth: true,
    });
    $('.your-class').slick({
        centerMode: true,
        centerPadding: '60px',
        slidesToShow: 3,
        responsive: [
          {
            breakpoint: 768,
            settings: {
              arrows: false,
              centerMode: true,
              centerPadding: '40px',
              slidesToShow: 3
            }
          },
          {
            breakpoint: 480,
            settings: {
              arrows: false,
              centerMode: true,
              centerPadding: '40px',
              slidesToShow: 1
            }
          }
        ]
      });
});