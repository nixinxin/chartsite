$(function() {
    $("#registerForm").bootstrapValidator({
        message: "此值无效！",
        feedbackIcons: {
            valid: "glyphicon glyphicon-ok",
            invalid: "glyphicon glyphicon-remove",
            validating: "glyphicon glyphicon-refresh"
        },
        fields: {
            name: {
                message: "姓名无效！",
                validators: {
                    notEmpty: {
                        message: "请输入姓名！"
                    },
                    regexp: {
                        regexp: /^[a-zA-Z0-9_\.]+$/,
                        message: "用户名只能包含字母，数字和下划线！"
                    }
                }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: "请输入邮箱！"
                    },
                    emailAddress: {
                        message: "请输入正确的邮箱地址！"
                    }
                }
            },
            password: {
                validators: {
                    notEmpty: {
                        message: "请输入密码！"
                    },
                    callback: {
                        callback: function (e, t) {
                            return e.length < 6 ? {
                                valid: !1,
                                message: "密码长度小于6！"
                            } : !0
                        }
                    }
                }
            },
            confirmPassword: {
                validators: {
                    notEmpty: {
                        message: "请输入确认密码！"
                    },
                    identical: {
                        field: "password",
                        message: "密码和确认密码是不一致！"
                    }
                }
            },
            verify: {
                validators: {
                    notEmpty: {
                        message: "请输入验证码！"
                    },
                    callback: {
                        callback: function (e, t) {
                            return 4 !== e.length ? {
                                valid: !1,
                                message: "请输入正确的验证码！"
                            } : ($.ajax({
                                async: !1,
								url: "/captcha/imagecode/?" + e,
                                type: "Get",
                                success: function (t, a) {
									alert(a);
									e = t;
									$('.captcha').attr("src",t.image_url);
									$('#id_captcha_0').attr("value",t.key);
								},
                                error: function (t, a) {
                                    e = a
                                }
                            }), "error" === e ? {
                                valid: !1,
                                message: "请输入正确的验证码！"
                            } : !0)
                        }
                    }
                }
            }
        }
    }).on("success.form.bv", function (e) {
        e.preventDefault();
        var t = $(this).serializeJSON();
        $.ajax({
            url: "/users/",
            type: "Post",
            data: $(this).serialize(),
            success: function (e) {
                console.log(e, e.status);
                heap.identify({
                    type: "new",
                    email: e.email
                }), BootstrapDialog.alert("注册成功！", function () {
                    var t = HZ.getParams();
                    if (t.callback) location.href = /index/;
                    else {
                        var a = "/user/login/" + e.ticket + "?new=1";
                        document.referrer && document.referrer !== document.location.origin + "/" && (a += "&ref=" + document.referrer), location.href = a
                    }
                })
            },
            error: function (e) {
                var a = $("#email"),
                    r = 500 === e.status ? "服务器繁忙，请稍后再试！" : e.responseText;
                BootstrapDialog.alert(r, function () {
                    $("#captcha").trigger("click"), $("#registerForm").data("bootstrapValidator").resetForm(!0), a.val(t.email), setTimeout(function () {
                        a.focus()
                    })
                })
            }
        })
    }),
        $(".captcha").click(function () {
            var e = $(this).attr("src").replace(/\?.*/, "");
            $(this).attr("src", e + "?" + Math.random()),
                $('input[name="verify"]').val("").focus(),
                $("form").bootstrapValidator("resetField", "verify"),
                $(":submit").attr("disabled", !0)
        })
    }
);