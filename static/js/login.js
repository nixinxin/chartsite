$(function () {
    $("button","#oAuth").click(
        function(){
            var e,a=$(this).attr("data-type");
            e &&(location.href="/login/"+a)})
});

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
        onkeydown:true,
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
                $.ajax({
                    url:"/users/1/",
                    type: 'get',
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
                        $.cookie('name', name, {expires:1, path: '/'});
                        user.addClass("profile");
                        $("#userInfo").empty().append('<a href="/personal" class="dropdown-toggle"><img class="img-circle" src='+ data.image +'>'+ name +'<b class="caret"></b> <span class="fa fa-envelope pull-right message" style="font-size:1.5em"><span class="navbar-unread count">10</span></span></a><ul id="userMenu" class="dropdown-menu" style="display:none"><li><a href="/personal">我的消息 <span class="fa fa-envelope pull-right"></span></a></li><li class="divider"></li><li><a href="/account">账号设置 <span class="glyphicon glyphicon-cog pull-right"></span></a></li><li class="divider"></li><li><a href="http://i.hubwiz.com/invite">邀请朋友 <span class="fa fa-users pull-right"></span></a></li><li class="divider"></li><li><a href="http://i.hubwiz.com/coupon">优惠券管理 <span class="fa fa-credit-card pull-right"></span></a></li><li class="divider"></li><li><a href="/index" id="logout">安全退出 <span class="glyphicon glyphicon-log-out pull-right"></span></a></li></ul>')
                     },
                })
            },
            error: function (data, status) {
                $("#user").removeClass('profile').empty().html(
                    '<li class="dropdown" id="userInfo"><a href="/user/login"><i class="fa fa-sign-in"></i> 登录 </a></li>' +
                    '<li><a href="/user/register"><i class="fa fa-pencil"></i> 注册</a></li>')
            }
    });
        },
    })
});

