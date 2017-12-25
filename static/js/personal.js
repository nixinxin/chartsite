$(function () {
    let user = $("#user");

    if(document.cookie.indexOf('name')+1 && !document.getElementById("userInfo")){
        $.ajax({
            url: "/users/1/",
            success: function (data, status) {
                let name;
                if (data.first_name) {
                    name = data.first_name
                }
                else {
                    name = data
                }
                if(!name){
                    name= data.email.substring(0,4)
                }
                user.addClass("profile");
                user.empty().append('<li id="userInfo" class="dropdown">' +
                    '                    <a href="/personal/" class="dropdown-toggle" >' +
                    '                        <img class="img-circle" src='+ data.image +'>' + name +
                    '                        <b class="caret"></b>' +
                    '                    <span class="fa fa-envelope pull-right message" style="font-size: 1.5em;"> <span class="navbar-unread count">1</span></span>' +
                    '                    <ul id="userMenu" class="dropdown-menu" style="display: none;">' +
                    '                        <li>' +
                    '                            <a href="/personal">我的消息' +
                    '                                <span class="fa fa-envelope pull-right"></span>' +
                    '                            </a>' +
                    '                        </li>' +
                    '                        <li class="divider"></li>' +
                    '                        <li><a href="/account">账号设置' +
                    '                                <span class="glyphicon glyphicon-cog pull-right"></span></a>' +
                    '                        </li>' +
                    '                        <li class="divider"></li>' +
                    '                        <li>' +
                    '                            <a href="http://i.hubwiz.com/invite">邀请朋友' +
                    '                                <span class="fa fa-users pull-right"></span>' +
                    '                            </a>' +
                    '                        </li>' +
                    '                        <li class="divider"></li>' +
                    '                        <li><a href="#" id="logout">安全退出' +
                    '                                <span class="glyphicon glyphicon-log-out pull-right"></span></a>' +
                    '                        </li>' +
                    '                    </ul>' +
                    '                </li>')
                $(".img-circle.avatar").attr("src", data.image);
                $(".right-user").find("h2").text(data.email).find("p").text(data.desc);
            },
        })
    }
    else{
        user.empty().append('<li><a href="/user/login"><i class="fa fa fa-sign-in"></i> 登录</a></li>');
        if (user.hasClass("profile")){
            user.removeClass("profile")
        }
        user.append('<li><a href="/user/register"><i class="fa fa-pencil"></i>  注册</a></li>');
    }
});

 