/*
Script: csyd-common.js
        封装常用业务相关的前端方法

Object: CSYD
	
Example:
	if(CSYD.isOnline()) { 
    //在线 TODO
    };
*/
CSYD = new function () {
    /***   判断用户是否在线  ****/
    this.isOnline = function () {
        var isonline = 0;
        $.ajax({
            url: _rootUrl+'/auth/IsOnline',
            type: 'post',
            async: false,
            success: function (data) {
                if (data.result) {
                    isonline = 1;//在线
                }
            },
            fail: function () {

            }
        });
        return isonline;
    };
    //获取caj下载url
    this.getCajUrl = function (filecode, pagerange,disk) {
        var url = "";
        var jsondata = { "filecode": filecode, "pagerange": pagerange, "disk": disk };
        $.ajax({
            url: _rootUrl+'/download/GetCajUrl',
            data: jsondata,
            type: 'post',
            async: false,
            success: function (data) {
                url = data.url;
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                //console.log(XMLHttpRequest.status);
                //console.log(XMLHttpRequest.readyState);
                //console.log(errorThrown);
            }
        });
        return url;
    };
    //获取pdf下载url
    this.getPdfUrl = function (filecode, pagerange, disk) {
        var url = "";
        var jsondata = { "filecode": filecode, "pagerange": pagerange, "disk": disk };
        $.ajax({
            url:_rootUrl+ '/download/GetPdfUrl',
            data: jsondata,
            type: 'post',
            async: false,
            success: function (data) {
                url = data.url;
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                //console.log(XMLHttpRequest.status);
                //console.log(XMLHttpRequest.readyState);
                //console.log(errorThrown);
            }
        });
        return url;
    };
    this.getKdocLogoutUrl = function () {
        var kdocLogoutUrl = "";
        $.ajax({
            url:_rootUrl+ '/auth/KdocLogoutUrl',
            type: 'post',
            async: false,
            success: function (data) {

                kdocLogoutUrl = data.url;

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {

            }
        });
        return kdocLogoutUrl;
    };
    this.kdocLogout = function () {
        try {
            var kdocLogoutUrl = this.getKdocLogoutUrl();

            $.ajax({
                url: kdocLogoutUrl,
                type: "post",
                dataType: 'jsonp',
                //jsonp的值自定义,如果使用jsoncallback,那么服务器端,要返回一个jsoncallback的值对应的对象. 
                jsonp: 'jsoncallback',
                //要传递的参数,没有传参时，也一定要写上 
                data: null,
                timeout: 5000,
                //返回Json类型 
                contentType: "application/json;utf-8",

                success: function (result) {

                },
                error: function (jqXHR, textStatus, errorThrown) {
                    //alert("A");
                }
            });
        } catch (e) {
            alert("catch:" + e.message);
        }
    };
    /***  是否为镜像版本   ****/
    this.isMirror = function () {
        var ismirror = 0;
        $.ajax({
            url:_rootUrl+ '/base/IsMirror',
            type: 'post',
            async: false,
            success: function (data) {
                if (data.result) {
                    ismirror = 1;//镜像
                }
            },
            fail: function () {

            }
        });
        return ismirror;
    };

   


    this.IsValid = function (inputObj) {
        re = /alter|select|update|delete|insert|exec|execute|count|drop|truncate|script|'|"/i;
        $sMsg = "请您不要输入特殊字符和关键字！"
        if (re.test(inputObj.val())) {
            alert($sMsg);
            inputObj.val('');
            inputObj.focus();
            return false;
        } else { return true; }
    };
    this.IsValidTxt = function (txt) {
        re = /alter|select|update|delete|insert|exec|execute|count|drop|truncate|script|'|"/i;
        //$sMsg = "请您不要输入特殊字符和关键字！"
        if (re.test(txt)) {
            return false;
        } else { return true; }
    };

    //获取url参数
    this.getUrlParameter = function (name) {
        var res = "";
        if (window.location.search.indexOf("?") != -1) {
            var url = window.location.search.substr(1);
            var params = url.split("&");

            for (var i = 0; i < params.length; i++) {
                if (params[i].split("=")[0] == name) {
                    res = params[i].split("=")[1];
                }
            }
        }
        return res;
    }
};