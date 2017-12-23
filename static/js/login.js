$(function() {
    $("#loginForm").bootstrapValidator({
		message: "此值无效！",
		feedbackIcons: {
			valid: "glyphicon glyphicon-ok",
			invalid: "glyphicon glyphicon-remove",
			validating: "glyphicon glyphicon-refresh"
		},
		fields: {
			username: {
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
					}
				}
			},
			verify: {
				validators: {
					notEmpty: {
						message: "请输入验证码！"
					},
					callback: {
						callback: function(e, t) {
							return 4 !== e.length ? {
								valid: !1,
								message: "请输入正确的验证码！"
							}:($.ajax({
								async: !1,
								url: "/verify/?response=" + e + "&hashkey=" + $("#id_captcha_0").val(),
								type: "Get",
								success: function(t, a) {
									e = t
								},
								error: function(t, a) {
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
	}).on("success.form.bv", function(e) {
		e.preventDefault(), $.ajax({
			url: "/login/",
			type: "Post",
			data: {
			    "csrfmiddlewaretoken": $("[name=csrfmiddlewaretoken]").val(),
			    "username": $("[name=username]").val(),
			    "password": $("[name=password]").val()
            },
			success: function(e, t) {
                if (e.token){
                     $.cookie('token',e.token, {"expired": 1});
                     $.get(
                         '/users/1/',
                         function (data) {
                             confirm(data)
                         }
                     )
                }

			},
			error: function(e) {
				500 === e.status ? BootstrapDialog.alert("服务器繁忙，请稍后再试！") : BootstrapDialog.alert(e.responseText), $("#email").focus(), $(":password").val(""), $("#captcha").trigger("click")
			}
		})
	}), $("button", "#oAuth").click(function() {
		var e, t, a = $(this).attr("data-type");
		switch (a) {
		case "qq":
			e = "https://graph.qq.com/oauth2.0/authorize?", t = ["response_type=code", "client_id=101161717", "redirect_uri=http://agridata.iask.in/complete/qq"];
			break;
		case "sina":
			e = "https://api.weibo.com/oauth2/authorize?", t = ["client_id=1064902839", "scope=all", "redirect_uri=http://agridata.iask.in/complete/weibo", "state=" + Date.now()];
			break;
		case "github":
			e = "https://github.com/login/oauth/authorize?", t = ["client_id=843129131eab9a3287a8", "redirect_uri=http://agridata.iask.in/complete/github", "state=" + Date.now()]
		}
		e && t && (location.href = e + t.join("&"))
	}), $(".captcha").click(function() {
		var e = $(this).attr("src").replace(/\?.*/, "");
		$(this).attr("src", e + "?" + Math.random()), $('input[name="verify"]').val("").focus(), $("form").bootstrapValidator("resetField", "verify"), $(":submit").attr("disabled", !0)
	})
});