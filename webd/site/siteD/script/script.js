$(function () {
    $(function () {
        currenIndex = 0;

        setInterval(function () {
            nextIndex = (currenIndex + 1) % 3

            $(".slider").eq(currenIndex).fadeOut(900);
            $(".slider").eq(nextIndex).fadeIn(900);

            currenIndex = nextIndex;
        }, 3000)
    })

    const tabButn = $(".title ul li");
    const tabCont = $(".cont > div");

    tabCont.hide().eq(0).show();

    tabButn.click(function (e) {
        e.preventDefault

        const index = $(this).index();

        $(this).addClass("active").siblings().removeClass("active")
        tabCont.eq(index).show().siblings().hide()
    })

    // 메뉴
    $(function () {
        $(".nav > ul > li").mouseover(function () {
            $(".nav > ul > li > ul").stop().fadeIn(900)
        });

        $(".nav > ul > li").mouseout(function () {
            $(".nav > ul > li > ul").stop().fadeOut(100)
        });
    });

    // 팝업
    $(".popup-btn").click(function () {
        $(".popup-view").show();
    });
    $(".popup-close").click(function () {
        $(".popup-view").hide();
    });
});