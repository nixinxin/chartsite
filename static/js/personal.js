
$(function () {
    let user = $("#user");
    let userInfo = $("#userInfo");
    if(document.cookie.indexOf('name')+1 && !document.getElementById("userMenu")){
        $.ajax({
            url: "/users/1/",
            success: function (data, status) {
                let name;
                if (data.first_name) {
                    name = data.first_name
                }
                else {
                    name = data.username
                }
                if(!name){
                    name= data.email.substring(0,4)
                }
                user.addClass("profile");
                $("#userInfo").empty().append('<a href="/personal" class="dropdown-toggle"><img class="img-circle" src='+ data.image +'>'+ name +'<b class="caret"></b> <span class="fa fa-envelope pull-right message" style="font-size:1.5em"><span class="navbar-unread count">10</span></span></a><ul id="userMenu" class="dropdown-menu" style="display:none"><li><a href="/personal">我的消息 <span class="fa fa-envelope pull-right"></span></a></li><li class="divider"></li><li><a href="/account">账号设置 <span class="glyphicon glyphicon-cog pull-right"></span></a></li><li class="divider"></li><li><a href="http://i.hubwiz.com/invite">邀请朋友 <span class="fa fa-users pull-right"></span></a></li><li class="divider"></li><li><a href="http://i.hubwiz.com/coupon">优惠券管理 <span class="fa fa-credit-card pull-right"></span></a></li><li class="divider"></li><li><a href="/index" id="logout">安全退出 <span class="glyphicon glyphicon-log-out pull-right"></span></a></li></ul>')
                $(".img-circle.avatar").attr("src", data.image);
                $(".right-user").find("h2").text(data.email).find("p").text(data.desc);
            },
        })
    }
    if(document.cookie.indexOf('name')=== -1){
        if (user.hasClass("profile")){user.removeClass("profile")}
        user.append('<li id="userInfo" class="dropdown"><a href="/user/login"><i class="fa fa-sign-in"></i>  登录</a></li>');
        user.append('<li><a href="/user/register"><i class="fa fa-pencil"></i>  注册</a></li>');
    }
});
 