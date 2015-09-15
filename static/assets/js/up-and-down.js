jQuery(function(){
    $("#Top").hide().removeAttr("href");
    if ($(window).scrollTop()>="200") $("#Top").fadeIn("slow")
    $(window).scroll(function(){
        if ($(window).scrollTop()<="200") $("#Top").fadeOut("slow")
        else $("#Top").fadeIn("slow")
    });

    $("#Bottom").hide().removeAttr("href");
    if ($(window).scrollTop()<=$(document).height()-"999") $("#Bottom").fadeIn("slow")
    $(window).scroll(function(){
        if ($(window).scrollTop()>=$(document).height()-"999") $("#Bottom").fadeOut("slow")
        else $("#Bottom").fadeIn("slow")
    });

    $("#Top").click(function(){
        $("html, body").animate({scrollTop:0},"slow");
        $($('.navmenu li.active a').attr('href')).next();
    })
    $("#Bottom").click(function(){
        if ($('.navmenu li.active').next().index() != -1) {
            var height_menuF = 0;

            if ($('#menuF').attr('class') == 'default') {
                height_menuF = $('#menuF').height();
            }

            $("html, body").animate({scrollTop: $($('.navmenu li.active').next().find('a').attr('href')).offset().top - 80 - height_menuF}, "slow");
        } else {
            $("html, body").animate({scrollTop:$(document).height()},"slow")
        }
    });
});