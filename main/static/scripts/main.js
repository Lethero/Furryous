$(document).ready(function() {
    /*
     * Hide navbar when scrolling down on phones.
     * Show when scrolling up.
     */
    var didScroll;
    var lastScrollTop = 0;
    var delta = 5;
    var navbarHeight = $('nav').outerHeight();

    // Detect the scroll
    $(window).scroll(function() {
        didScroll = True;
    });

    // Every 250ms, check to see if the user scrolled
    setInterval(function() {
        if (didScroll) {
            hasScrolled();
            didScroll = false;
        }
    }, 250);

    function hasScrolled() {
        // Check to see if window size is table size or smaller.
        if ($(window).width() < 1000) {
            var st = $(this).scrollTop();
            if (Math.abs(lastScrollTop - st) <= delta) return;
            if (st > lastScrollTop && st > navbarHeight) {
                $('nav').addClass('nav-up');
            } else {
                if (st + $(window).height() < $(document).height()) {
                    $('nav').removeClass('nav-up');
                }
            }

            lastScrollTop = st;
        }
    }

    // When toggle display is clicked
    $(".toggle-display").click(function(event) {
        event.preventDefault();

        // Toggle active class of the clicked element.
        $(this).toggleClass("active");

        // Get the target
        var target = $($(this).data("target"));

        // Slide toggle the element and add display flex.
        target.slideToggle('slow', function() {
            if ($(this).is(":visible")) {
                $(this).css("display", "flex");
            }
        });
    });
});