$(document).ready(function() {
    // header active scroll
    $(function() {
        let header = $('.header');

        $(window).scroll(function() {
            if ($(this).scrollTop() > 2) {
                header.addClass('active');
            } else {
                header.removeClass('active');
            }
        });
    });

    // menu-link active 
    $('.menu-link').on('mouseenter', function() {
        $('.menu-link').removeClass('active');
        $(this).addClass('active');
    });
    $('.menu-link').on('mouseleave', function() {
        $('.menu-link').removeClass('active');
    });
    $('.menu-link').on('click', function() {
        $('.menu-link').addClass('active');
    });
    // phone active
    $('.phone').on('mouseenter', function() {
        $('.phone-icon').addClass('active');
    });
    $('.phone').on('mouseleave', function() {
        $('.phone-icon').removeClass('active');
    });

    // gamburger menu
    $(function() {
        const $menu_popup = $('.menu-popup');

        $(".menu-triger").click(function() {
            $menu_popup.addClass('active')
        });

        $(".menu-close").click(function() {
            $menu_popup.removeClass('active')
        });

        $(document).on('click', function (e) {
            if (!$(e.target).closest('.menu-popup').length && !$(e.target).closest('.menu-triger').length) {
                $menu_popup.removeClass('active');
            }
        });
    });

    // tabs-menu shop
    $('.shop-navigation_button').on('click', function() {

        let currTab = $(this).parent().index();
        $('.shop-navigation_button').removeClass('active');
        $(this).addClass('active');

        $('.shop-catalog_list').removeClass('active');
        $('.shop-catalog_list').eq(currTab).addClass('active');
    });
});

const infoSlider = new Swiper('.info-slider', {
    // Optional parameters
    autoplay: {
        delay: 5000,
    },
    slidesPerView: "1",
    spaceBetween: 30,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        type: 'bullets',
        bulletClass: 'dot',
        bulletActiveClass: 'active-dot',

    },
    preloadImages: false,
});


const teamSlider = new Swiper('.team-slider', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
    preloadImages: false,

    // If we need pagination
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        type: 'bullets',
        bulletClass: 'dot',
        bulletActiveClass: 'team-active_dot',
    },
});