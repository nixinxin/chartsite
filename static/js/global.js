
function getCookie(cname) {
    let name = cname + "=";
    let ca = document.cookie.split(';');
    for(let i=0; i<ca.length; i++) {
        let c = ca[i].trim();
        if (c.indexOf(name)===0) return c.substring(name.length,c.length);
    }
    return "";
}

$(function () {
    let user = $("#user");
    let userInfo = $("#userInfo");
    if((getCookie("name")) && !document.getElementById("userMenu")){
        $.ajax({
            url: "/users/1/",
            success: function (data, status) {
                let name = data.first_name || data.username;
                let user = $("#user");
                user.addClass("profile");
                user.find("li:first a").empty().append('<img class="img-circle" src='+ data.image +'>'+ name +'<b class="caret"></b> <span class="fa fa-envelope pull-right message" style="font-size:1.5em"><span class="navbar-unread count">10</span></span>');
                user.find("li:first").append('<ul id="userMenu" class="dropdown-menu" style="display:none"><li><a href="/personal">个人中心<span class="fa fa-envelope pull-right"></span></a></li><li class="divider"></li><li><a href="/account">账号设置 <span class="glyphicon glyphicon-cog pull-right"></span></a></li><li class="divider"></li><li><a href="/invite">邀请朋友 <span class="fa fa-users pull-right"></span></a></li><li class="divider"></li><li><a href="/index" id="logout">安全退出 <span class="glyphicon glyphicon-log-out pull-right"></span></a></li></ul>');
                user.remove("li:even")
            },
        })
    }
    else{
        if (user.hasClass("profile")){user.removeClass("profile")}
        user.append('<li id="userInfo" class="dropdown"><a href="/user/login"><i class="fa fa-sign-in"></i>  登录</a></li>');
        user.append('<li><a href="/user/register"><i class="fa fa-pencil"></i>  注册</a></li>');
    }
});

$(function(){
    //刷新验证码
    $(".captcha").click(function(){
        $.get("/captcha/refresh/?"+Math.random(), function(result){
                $("#id_captcha_1").val('').focus();
                $('.captcha').attr("src",result.image_url);
                $('#id_captcha_0').attr("value",result.key);
            });
    });
    $("#logout").click(function () {
        delete document.cookie;
        window.location.href = '/index/'
    });
    $("#labBtn").click(function(){location.href="/share/"});
});

$(document.getElementById("userInfo")&&($("#userInfo").hover(function(){$("#userMenu").stop().slideDown("fast")},function(){$("#userMenu").slideUp("fast")})));
$(function(){if(!/^\/(class)|(book)/.test(location.pathname)){var e=$("<div>").attr("id","fixedTools").addClass("hidden-xs hidden-sm").append($("<i>").addClass("glyphicon glyphicon-circle-arrow-up")).appendTo("body");$(window).scroll(function(){0!=$(this).scrollTop()?e.fadeIn():e.fadeOut()}),e.click(function(){return $("html, body").animate({scrollTop:0},300),!1})}$('a[href="'+document.location.pathname+'"]',"#hb-nav>li").parent().addClass("active"),document.getElementById("userInfo")&&($("#userInfo").hover(function(){$("#userMenu").stop().slideDown("fast")},function(){$("#userMenu").slideUp("fast")}))});
