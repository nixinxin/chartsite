// dom加载完成后执行
$(function () {
    //zhushis111
    /*扩展指标弹出层初始化*/
    //ShowDialog.init($("#J_extend,#J_yearLayout"));

    /*.nav 子菜单list超出省略*/
    var libstringObjs = $("#J_tablist3,#J_tablist4,#J_jidu,#J_yuedu").find("a");
    var J_tablist5 = $("#J_tablist5").find("p").find("a");
    libstringObjs.each(function () {
        LIBSTRING.cut($(this), 145);
    });
    J_tablist5.each(function () {
        LIBSTRING.cut($(this), 123);
    });

    /*  为主导航绑定hover事件*/
    $("#J_nav").find(".J_mnav").hover(function () {
        var _this = $(this),
    index = $("#J_nav").find(".J_mnav").index(this);
        var tabcon = $("#J_nav").find(".tabcon").eq(index);
        tabcon.removeClass(" vhide ");
        tabcon.css({ zIndex: 8 });
    }, function () {
        var _this = $(this),
    index = $("#J_nav").find(".J_mnav").index(this);
        var tabcon = $("#J_nav").find(".tabcon").eq(index);
        tabcon.addClass(" vhide ");
    });

    /*次导航绑定click事件*/
    $("#Y_mlist_nav").find("span").click(function () {
        $("#Y_mlist_nav").find("span").removeClass("current");
        $(this).addClass("current");
        var n = $(this).index();
        $(".Y_slist").removeClass("show").addClass("hide");
        $("#Y_slist_" + n).removeClass("hide").addClass("show");
    });

    /*input添加placeholder涉及的获得焦点和失去焦点事件*/
    var plds = $(".fpacehd");
    setPlaceHolder(plds);


    /*.accordion 初始化*/
    Accordion.init($(".accordion"));

});
/*---------------------------------------------------------------------------*/



/*公共方法=============================================*/
// 设置输入框默认提示信息
function setPlaceHolder(objs) {
    if (objs && objs.size() > 0) {
        objs.each(function () {
            var _this = $(this);
            var oid = $(this).attr("for");
            var oinput = $("#" + oid);
            _this.click(function () {
                $(this).hide();
                oinput.focus();
            });
            oinput.focusout(function () {
                if (!$(this).val()) {
                    _this.show();
                }
            }).focusin(function () {
                _this.hide();
            });
        });
    }
}


/*字符串截取类================*/
var LIBSTRING = (function () {
    var LIBSTRING = function () {
        return LIBSTRING.fn.init();
    };
    LIBSTRING.fn = LIBSTRING.prototype = {
        init: function () {
            return this;
        }
    };
    LIBSTRING.fn.length = function (str) {
        return str ? str.replace(/[^\x00-\xff]/g, "aa").length : 0;
    };
    LIBSTRING.fn.cutLen = function (str, len, cut) {
        var _str = str;
        if (!str || !len || this.length(str) <= len * 2) {
            return str;
        } else {
            var m = Math.floor(len / 2);
            for (var i = m; i < str.length; i++) {
                if (this.length(str.substr(0, i)) >= len * 2) {
                    var newStr = str.substr(0, i) + cut;
                    var wrapstr = "<span title='" + _str + "'>" + newStr + "</span>";
                    return wrapstr;
                }
            }
            return str;
        }

    }
    LIBSTRING.fn.cut = function (obj, mwidth, tlen) {
        if (!obj || !obj.length) return;
        tlen < 1 || (tlen = 15);
        $(obj).html(this.cutLen($(obj).html(), parseInt((mwidth || $(obj).width()) / tlen), "..."));
    };
    return LIBSTRING();
})();
/*字符串截取类 end================*/


/*Accordion对象 start=============*/
; (function ($) {
    var Accordion = function (ad) {
        this.ad = ad;
        this.bindClick();
    };
    Accordion.prototype = {
        bindClick: function () {
            var _this = this;
            _this.ad.on("click", ".adtit", function () {
                $(this).next(".adCon").show().siblings(".adCon").hide();
                $(".J_iscrollbox-tree").each(function () {
                    $(this).removeData("iscrollbar").iScrollbar({
                        "speed": 50,
                        "animH": 253,
                        "lineH": 28,
                        "listClass": "jstree-container-ul"
                    });
                });
            });
        }
    };
    Accordion.init = function (ads) {
        var _this = this;
        ads.each(function () {
            new _this($(this));
        });
    }
    window["Accordion"] = Accordion;
})(jQuery);
/*Accordion对象 end===========*/

/*dialog对象 start*/
(function ($) {
    var ShowDialog = function (dialogBox) {
        this.setting = { "speed": "500", "maskClass": "mask", "dialogID": "" };
        this.dialogBox = dialogBox;
        $.extend(this.setting, this.getSetting());
        this.mask = $("." + this.setting.maskClass);
        if ($.trim(this.setting.dialogID) != "") {
            this.showBox = $("#" + this.setting.dialogID);
            this.dialogHtml = this.showBox.html();
            this.initMast();
        } else {
            ////console.log("dialogBox:data-setting dialogID值为空");
            return false;
        }
    };

    ShowDialog.prototype = {
        /*获取外部设置的参数*/
        getSetting: function () {
            var settings = this.dialogBox.attr("data-setting");
            if (settings && settings != "") {
                return $.parseJSON(settings);
            } else {
                return {};
            }
        },
        /*绑定点击事件*/
        show: function () {
            var _this = this;
            try {
                _this.mask.removeClass("hide");
                _this.showBox.removeClass("vhide");
                var windowH = $(window).height();
                var selfH = _this.showBox.outerHeight(true);
                var otop = (windowH - selfH) / 2;
                if (navigator.appName == "Microsoft Internet Explorer" && navigator.appVersion.split(";")[1].replace(/[ ]/g, "") == "MSIE7.0") {
                    otop = otop + $(window).scrollTop();
                }
                _this.showBox.stop().animate({
                    "top": otop + "px"
                }, _this.setting.speed);
                _this.bindCloseBtnClick();
            } catch (e) {
                //console.log("ShowDialog出现错误，错误信息：" + e.message);
                return false;
            }
        },
        /*初始化弹出层宽 高*/
        initMast: function () {
            var _this = this;
            _this.mask.height($(document).height());
            // 浏览器窗口尺寸变化时重新设置遮罩层高
            $(window).resize(function () {
                _this.mask.height($(document).height());
                var windowH = $(window).height();
                var selfH = _this.showBox.outerHeight(true);
                var otop = (windowH - selfH) / 2;
                if (navigator.appName == "Microsoft Internet Explorer" && navigator.appVersion.split(";")[1].replace(/[ ]/g, "") == "MSIE7.0") {
                    otop = otop + $(window).scrollTop();
                }
                if (otop < 0) {
                    otop = 0;
                }
                _this.showBox.stop().animate({
                    "top": otop + "px"
                }, _this.setting.speed);
            });
        },
        close: function () {
            var _this = this;
            _this.showBox.addClass(" vhide ").attr("style", "");
            _this.mask.addClass(" hide ");
            _this.showBox.html(_this.dialogHtml);
        },
        /*关闭按钮 绑定点击事件*/
        bindCloseBtnClick: function () {
            var _this = this;
            _this.showBox.find(".btn-close").on("click", function () {
                _this.close();
            });
        }
    };

    // 初始化
    ShowDialog.init = function (dialogBoxs) {
        var _this = this;
        if (dialogBoxs && $.trim(dialogBoxs) != "") {
            dialogBoxs.each(function () {
                new _this($(this));
            });
        }
    };
    window["ShowDialog"] = ShowDialog;
})(jQuery);
/*dialog对象 end*/