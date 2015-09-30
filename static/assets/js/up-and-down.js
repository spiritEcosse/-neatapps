jQuery(function(){
    $("#Top").hide().removeAttr("href");

    if ($(window).scrollTop()>="200") {
        $("#Top").fadeIn('fast');
    }

    $(window).scroll(function(){
        if ($(window).scrollTop()<="200") {
            $("#Top").fadeOut('fast');
        }else {
            $("#Top").fadeIn('fast');
        }
    });

    $("#Bottom").hide().removeAttr("href");

    if ($(window).scrollTop()<=$(document).height()-"999") {
        $("#Bottom").fadeIn('fast');
    }

    $(window).scroll(function(){
        if ($(window).scrollTop()>=$(document).height()-"999") {
            $("#Bottom").fadeOut('fast');
        } else {
            $("#Bottom").fadeIn('fast');
        }
    });

    $("#Top").click(function(){
        $(this).css('display', 'none');
        $("html, body").animate({scrollTop:0},"slow");
        $($('.navmenu li.active a').attr('href')).next();
    });
    $("#Bottom").click(function(){
        if ($('.navmenu li.active').next().index() != -1) {
            var height_menuF = 0;

            if ($('#menuF').attr('class') == 'default') {
                height_menuF = $('#menuF').height();
            }

            $("html, body").animate({scrollTop: $($('.navmenu li.active').next().find('a').attr('href')).offset().top - 80 - height_menuF}, "slow");
        } else {
            $(this).css('display', 'none');
            $("html, body").animate({scrollTop:$(document).height()},"slow");
        }
    });
});