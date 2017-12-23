$(function() {
    $("#loginForm").validate({
        rules: {
            username: {
                required: true,
                email: true
            },
            password: {
                required: true,
                rangelength: [8, 20],
            },
            // response: {
            //     required: true,
            //     minlength: 4,
            //     maxlength: 4,
            //     remote: {
            //         url: "/verify/",     //后台处理程序
            //         type: "post", //数据发送方式
            //         data:{
            //             "hashkey": function(){
            //                 return $("#id_captcha_0").val()
            //             },
            //         },
            //         }
            //     },
            },
        message: {
            username: {
                required: "请输入合法的邮箱",
                email: "请输入合法的邮箱"
            },
            password: {
                required: "请输入密码",
                rangelength: "密码至少包一个大写字母、一个小写字母及一个符号，长度至少8位",
            },
            response: {
                required: true,
                minlength: '验证码不正确',
                maxlength: "验证码不正确",
                remote: "验证码不正确",
            },
        },
        errorClass: 'has-error',
        errorElement: "small",
        focusCleanup: true,
        keyup: true,
        success: function (element) {
            element.parent().parent().removeClass('has-error');
            element.parent().parent().addClass('has-success');
            element.parent().children("i").removeClass('glyphicon-remove');
            element.parent().children("i").addClass('glyphicon-ok');
            element.parent().children('small').remove()
        },
        errorPlacement: function (error, element) {
            element.parent().parent().parent().removeClass('has-success');
            element.parent().parent().children("i").removeClass('glyphicon-ok');
            element.parent().parent().children("i").addClass('glyphicon-remove');
            element.parent().parent().parent().addClass('has-error');
            element.parent().parent().append(error);
            element.parent().parent().children('small').addClass("alert alert-danger")
        },
        submitHandler:function (form) {
            $.ajax({url:"/login/",
                type:"Post",
                data:$(form).serialize(),
                success: function (data, status) {
                    $.cookie('token', data.token, {
                        path: '/',
                        expired: 7,
                    });
                    if(data.token){
                        $.ajax({
                        url:"/users/1/",
                        type: 'get',
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
                },
                error: function (data, status) {
                    alert("用户名或密码错误！")
                }
        });
        },
    });
});

