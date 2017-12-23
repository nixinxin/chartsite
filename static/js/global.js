
$("#labBtn").click(function(){location.href="/share/"});
$(function () {
    if ($.cookie("token")){
        $.ajax({
        url:"/users/1/",
        beforeSend: function (xhr) {
            // //发送ajax请求之前向http的head里面加入验证信息
            xhr.setRequestHeader("token", $.cookie('token')); // 请求发起前在头部附加token
        },
        success: function(data,status){
            $(".nav.navbar-nav.navbar-right").addClass("profile");
            $(".nav.navbar-nav.navbar-right").html("<li id=userInfo class=dropdown>" +
                "                    <a href='/personal' class='dropdown-toggle' data-token="+ $.cookie("token") +">" +
                "                        <img class='img-circle' src="+ data.image +">" + data.username +
                "                        <b class='caret'></b>" +
                "                        <span class='fa fa-envelope pull-right message' style='font-size: 1.5em; display: none;'>" +
                "                        <span class='navbar-unread count'>100</span></span>" +
                "                    </a>" +
                "                    <ul id='userMenu' class='dropdown-menu' style='display: none;'>" +
                "                        <li>" +
                "                            <a href='/personal'>个人中心" +
                "                                <span class='fa fa-envelope pull-right'></span>" +
                "                            </a>" +
                "                        </li>" +
                "                        <li class='divider'></li>" +
                "                        <li><a href='/account'>账号设置" +
                "                                <span class='glyphicon glyphicon-cog pull-right'></span></a>" +
                "                        </li>" +
                "                        <li class='divider'></li>" +
                "                        <li>" +
                "                            <a href='http://i.hubwiz.com/invite'>邀请朋友" +
                "                                <span class='fa fa-users pull-right'></span>" +
                "                            </a>" +
                "                        </li>" +
                "                        <li class='divider'></li>" +
                "                        <li><a href='/logoff'>安全退出" +
                "                                <span class='glyphicon glyphicon-log-out pull-right'></span></a>" +
                "                        </li>" +
                "                    </ul>" +
                "                </li>")

        }
    })
    }
});
