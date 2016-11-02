var mn = $(".navbar");
var mns = "scrolled";
var hdr = $("#header").outerHeight(true);

$(window).scroll(function() {
    if( $(this).scrollTop()>hdr ) {
        mn.addClass(mns);
    } else {
        mn.removeClass(mns);
    }
});
