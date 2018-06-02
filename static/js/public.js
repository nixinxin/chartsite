
/*公共方法=============================================*/


// 设置输入框默认提示信息
function setPlaceHolder(objs){
    if(objs&&objs.size()>0){
         objs.each(function(){
            var _this=$(this);
            var oid=$(this).attr("for");
            var oinput= $("#"+oid);
              _this.click(function(){
                    $(this).hide();
                   oinput.focus();
              });
              oinput.focusout(function(){
                  if(!$(this).val()){
                       _this.show();
                  }
              }).focusin(function(){
                  _this.hide();
                  oinput.focus();
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
        var _str=str;
        if (!str || !len || this.length(str) <= len * 2) {
            return str;
        }else{
             var m = Math.floor(len / 2);
                for (var i = m; i < str.length; i++) {
                    if (this.length(str.substr(0, i)) >= len * 2){
                        var newStr=str.substr(0, i) + cut;
                        var wrapstr="<span title='"+_str+"'>"+newStr+"</span>";
                          return wrapstr;
                      }
                    }
                return str;
        }
       
        } 
     LIBSTRING.fn.cutLen1 = function (str, len, cut) {
        if (!str || !len || this.length(str) <= len * 2) return str;
        var m = Math.floor(len / 2);
        for (var i = m; i < str.length; i++) {
            if (this.length(str.substr(0, i)) >= len * 2)
                return str.substr(0, i) + cut;
        }
        return str;
    };
      /*截取  有title*/
    LIBSTRING.fn.cut = function (obj, mwidth, tlen) {
        if (!obj || !obj.length) return;
        tlen < 1 || (tlen = 15);
        $(obj).html(this.cutLen($(obj).html(), parseInt((mwidth || $(obj).width()) / tlen), "..."));
    };
    /*父节点上添加title */
     LIBSTRING.fn.cut2 = function (obj, mwidth,pele, tlen) {
        if (!obj || !obj.length) return;
        tlen < 1 || (tlen = 15);
        var str=$(obj).html();
        $(obj).html(this.cutLen1($(obj).html(), parseInt((mwidth || $(obj).width()) / tlen), "...")).parent(pele).attr("title",str);
    };
      /*仅截取  无title*/
    LIBSTRING.fn.cut1 = function (obj, mwidth, tlen) {
        if (!obj || !obj.length) return;
        tlen < 1 || (tlen = 15);
        $(obj).html(this.cutLen1($(obj).html(), parseInt((mwidth || $(obj).width()) / tlen), "..."))
    };
    return LIBSTRING();
})();

/*字符串截取类 end================*/


/*设置超出隐藏 */
function setOverflowHide(objs,type,len,pele){
    var obj={
                    "str":function(ele){
                    try{
                        LIBSTRING.cut1(ele,len);
                    }catch(e){//失败添加样式.tbreak 超出省略...
                        $(this).addClass(" tbreak ");
                      //console.log("文本超出截取失败:"+e.message);
                    }
                },
                "str-title":function(ele){
                    try{
                        LIBSTRING.cut(ele,len);
                    }catch(e){//失败添加样式.tbreak 超出省略...
                        $(this).addClass(" tbreak ");
                      //console.log("文本超出截取失败:"+e.message);
                    }
                },
                "str-title-p":function(ele){
                    try{
                        LIBSTRING.cut2(ele,len,pele);
                    }catch(e){//失败添加样式.tbreak 超出省略...
                        $(this).addClass(" tbreak ");
                      //console.log("文本超出截取失败:"+e.message);
                    }
                }};

         if( objs&&objs.size()>0&&$.isNumeric(len)&&type!=""){
              objs.each(function(){
                   obj[type]($(this));
              });
         }else{
            return false;
         }
}

/*设置超出隐藏 */

 /*.nav 子菜单list超出省略*/
    var libstringObjs=$("#J_tablist3,#J_tablist4,#J_jidu,#J_yuedu").find("a");
    var J_tablist5=$("#J_tablist5").find("p").find("a");
    libstringObjs.each(function(){
         LIBSTRING.cut($(this),145);
    });
    J_tablist5.each(function(){
        LIBSTRING.cut($(this),123);
    });
   
 /*  为主导航绑定hover事件*/
 $("#J_nav").find(".J_mnav").hover(function(){
    var _this=$(this),
    index=$("#J_nav").find(".J_mnav").index(this);
    var  tabcon=$("#J_nav").find(".tabcon").eq(index);
     tabcon.removeClass(" vhide ");
    tabcon.css({zIndex:8});
 },function(){
    var _this=$(this),
    index=$("#J_nav").find(".J_mnav").index(this);
    var  tabcon=$("#J_nav").find(".tabcon").eq(index);
    tabcon.addClass(" vhide ");
 });
/*add 9-23 cjh 调用自定义滚动条  依赖jquery.self.iscroll.js*/
 function autoIscrollbar(iscrollbox,options,fn){
    !$.isEmptyObject(iscrollbox)&&iscrollbox.removeData("iscrollbar").iScrollbar(options,fn)||alert("fn:autoIscrollbar参数iscrollbox不正确！");
    return false;
}

//获取url字符串的值
var getQueryString = function (name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg); 
    if (r != null) return unescape(r[2]); return null;
}

//显示左侧指标树形分类
var showCateogorys = function (id) {
    $("#" + id).parent().show().siblings(".adCon").hide();
}

//显示指标模块
var showIndicates = function () {
    var obj = $(".floor2").find(".J_tit");
    var jtitlist = $(obj).siblings(".J_tit_list");
    var pdiv = $(obj).parent("div");
    obj.find(".icon-gt-right").addClass(" icon-gt-down ");
    jtitlist.removeClass("hide");
    pdiv.siblings("div").find(".J_tit_list").removeClass("hide");
    pdiv.siblings("div").find(".icon-gt-right").addClass(" icon-gt-down ");
    pdiv.parent(".floor").siblings(".floor").find(".J_tit_list").addClass(" hide ");
    pdiv.parent(".floor").siblings(".floor").find(".icon-gt-down").removeClass("icon-gt-down");
}
 
 /*------标红------*/
 var fnMark = function (str) {
     var reg1 = /#{3}/g;
     var reg2 = /\${3}/g;
     str = str.replace(reg1, '<span class="red">').replace(reg2, '</span>');
     return str;
 }




 $(document).ready(function () {
     var b_name = navigator.appName;
     var b_version = navigator.appVersion;
     var version = b_version.split(";");
     var trim_version = (version[1]||version[0]).replace(/[ ]/g, "");
     if (b_name == "Microsoft Internet Explorer") {
         if (trim_version == "MSIE8.0" || trim_version == "MSIE7.0" || trim_version == "MSIE6.0") {
             alert("由于您浏览器选择的内核版本过低，无法正常显示。\n\n若您使用360等双核浏览器，请切换为极速模式；IE浏览器等请升级或关闭兼容性视图！");         
            
         }
     }
 });