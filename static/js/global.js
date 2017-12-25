
$(function () {
    if (!$.cookie('token')) {
        let user = $("#user");
        user.empty().append('<li><a href="/user/login"><i class="fa fa fa-sign-in"></i>登录</a></li>');
        if (user.hasClass("profile")){
            user.removeClass("profile")
        }
        user.append('<li><a href="/user/register"><i class="fa fa-pencil"></i> 注册</a></li>');
    }
    else {
        $.ajax({
            url: "/users/1/",
            beforeSend: function (xhr) {
                // //发送ajax请求之前向http的head里面加入验证信息
                xhr.setRequestHeader("Authorization", "token " + document.cookie); // 请求发起前在头部附加token
            },
            success: function (data, status) {
                let name;
                let userinfo = $("#userInfo");
                if (data.first_name) {
                    name = data.first_name
                }
                else {
                    name = data.email
                }
                user.find("li:first").attr({"id": "userInfo", "class": 'dropdown'});
                userinfo.find("a").attr({"href": "/personal", "class": "dropdown-toggle"}).empty();
                userinfo.append('<img class="img-circle" alt="个人头像"  src='+ data.image +'>');
                userinfo.find("img").text(name);
                userinfo.append('<b class="caret"></b>');
                userinfo.append('<span class="fa fa-envelope pull-right message" style="font-size: 1.5em; display: none;"> <span class="navbar-unread count">100</span></span>')

            },
        })
    }
});



$(function(){
    $.get("/captcha/refresh/?"+Math.random(), function(result){
            $("#id_captcha_1").val('');
            $('.captcha').attr("src",result.image_url);
            $('#id_captcha_0').attr("value",result.key);
        });

    //刷新验证码
    $(".captcha").bind("click",function(){
        $.get("/captcha/refresh/?"+Math.random(), function(result){
                $("#id_captcha_1").val('').focus();
                $('.captcha').attr("src",result.image_url);
                $('#id_captcha_0').attr("value",result.key);
            });
    });
    $("#logout").click(function () {
        delete document.cookie;
    });
    $("#labBtn").click(function(){location.href="/share/"});
});





