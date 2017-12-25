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
            if(1){
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
                             let name;
                            if (data.first_name){name = data.first_name}
                            else {name = data.email}
                            $(".img-circle").attr("src", data.iamge).text(name);
                        }
                    })
                    }
                },
                error: function (data, status) {
                    user.removeClass('profile').empty().html(
                        '<li><a href="/user/login"><i class="fa fa-sign-in"></i> 登录 </a></li>' +
                        '<li><a href="/user/register"><i class="fa fa-pencil"></i> 注册</a></li>')
                }
        });
            }

        },
    })
});

