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
							}: ($.ajax({
								async:!1,
								url:"/verify/?" + $("#id_captcha_1").serialize() + "&" + $("#id_captcha_0").serialize(),
								// url:"/verify/?" + $("#id_captcha_1").serialize() + "&" + $("#id_captcha_0").serialize(),
								type:"Get",
								success:function(t,a){e=t, alter(this.url)},
								error:function(t,a){e=a}}),
								"error"===e?{valid:!1,message:"请输入正确的验证码！"}:!0)
						}
					}
				}
			}
		}
	}).on("success.form.bv", function(e) {
		e.preventDefault(), $.ajax({
			url: "/login/",
			type: "Post",
			data: $(this).serialize(),
			success: function(e) {
					$.cookie(e);
					location.href = /index/;
			},
			error: function(e) {
				500 === e.status ? BootstrapDialog.alert("用户未注册！") : BootstrapDialog.alert(e.responseText), $("#email").focus(), $(":password").val(""), $("#captcha").trigger("click")
			}
		})
	}), $("button", "#oAuth").click(function() {
		var e, t, a = $(this).attr("data-type");
		switch (a) {
		case "qq":
			e = "https://graph.qq.com/oauth2.0/authorize?", t = ["response_type=code", "client_id=101161717", "redirect_uri=http://agridata.iask.in/complete/qq"];
			break;
		case "sina":
			e = "https://api.weibo.com/oauth2/authorize?", t = ["client_id=1960899492", "scope=all", "redirect_uri=http://agridata.iask.in/complete/weibo/", "state=" + Date.now()];
			break;
		case "github":
			e = "https://github.com/login/oauth/authorize?", t = ["client_id=843129131eab9a3287a8", "redirect_uri=http://agridata.iask.in/complete/github", "state=" + Date.now()]
		}
		e && t && (location.href = e + t.join("&"))
	}), $(".captcha").click(function() {
		var e = $(this).attr("src").replace(/\?.*/, "");
		$(this).attr("src", e + "?" + Math.random()), $('input[name="verify"]').val("").focus(), $("form").bootstrapValidator("resetField", "verify"), $(":submit").attr("disabled", !0)
	})
}); +
function(o) {
	o.fn.autoShadow = function(a) {
		var s = {};
		o.extend(s, a);
		return this.each(function() {
			var a = this;
			o(window).scroll(function() {
				var s = document.body.scrollTop;
				0 >= s && o(a).hasClass("docs-nav-shadow") && o(a).removeClass("docs-nav-shadow"), s > 0 && !o(a).hasClass("docs-nav-shadow") && o(a).addClass("docs-nav-shadow")
			})
		})
	}, o(function() {
		o(".docs-nav").autoShadow()
	})
}(jQuery);
