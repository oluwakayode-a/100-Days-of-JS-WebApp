(function ($) {
    $(function () {
        $('.sidenav').sidenav();
        $('.dropdown-trigger').dropdown();
        $('.slider').slider({
            fullWidth: true,
            indicators: false,
            height: 500
        });
        $('input#icon_prefix').characterCounter();
        $('.parallax').parallax();
        $('.modal').modal();
    });
})(jQuery);


