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

    /*仿下拉菜单初始化  .selectbox 其他非下拉菜单不可使用该样式*/
    Selectbox.init($("#J_areaList,#J_subArealist,#J_areaTypelist"));

    /*checkbox初始化*/
    Checkbox.init($("#J_checkboxlist-area,#J_checkboxlist-target,#J_checkboxlist-time"));

    /*年度数据分析 已选列表 start===============*/
    //1、设置超出省略 列表中有默认值时用，无可不用设置超出省略
    $(".selectedlist").find("span").each(function () {
        LIBSTRING.cut($(this), 230);
    });
    //2、为已选择列表中的删除按钮绑定点击事件
    $(".selectedlist").on("click", ".btn-del", function () {
        var _this = $(this);
        var rel = _this.siblings(".checkedTxt").attr("rel");
        var txt = _this.siblings(".checkedTxt").find("span").size() == 0 ? _this.siblings(".checkedTxt").text() : _this.siblings(".checkedTxt").find("span").text();
        /* addAndUpdate 9-23 cjh start*/
        var list = _this.parent().parent(".selectedlist");
        var checklistID = list.attr("data-checksId");
        var J_iscroll = list.parent(".J_iscroll-selected");
        /* addAndUpdate 9-23 cjh  end*/
        var checklistID = _this.parent().parent(".selectedlist").attr("data-checksId");
        _this.parent("li").remove();
        var curCheckbox = $("#" + checklistID).find(".checkbox[rel='" + rel + "']");
        curCheckbox.removeClass("checkbox-checked").attr("data-checked", "");
        if (curCheckbox.siblings(".btn-icheckAll[data-checked='true']").size() == 1 && curCheckbox.siblings(".checkbox[data-checked='true']").size() == 0) {
            curCheckbox.siblings(".btn-icheckAll[data-checked='true']").removeClass("checkbox-checked").attr("data-checked", "");
        }
        /*调用自定义滚动条方法 add 9-23 cjh*/
        autoIscrollbar(J_iscroll, {
            "speed": 50,
            "animH": 391,
            "lineH": 28,
            "setTop0": false
        }, function () {
            var listId = list.attr("id");
            var otop = parseFloat($("#" + listId).css("top"));
            if (otop < 0) { //有翻页时每删除一个li ，J_iScrollbar-list的top值+lineH
                $("#" + listId).css("top", otop + 28);
            }
        });
    });
    /*年度数据分析 已选列表 end==================*/
    /*初始化map*/
    Map.init($("#J_smallMap"));

    /*年度数据分析中.floor  .J_tit 添加点击事件 实现.J_tit_list折叠、展开效果 */
    $(".floor").on("click", ".J_tit", function () {
        var _this = $(this);
        var jtitlist = _this.siblings(".J_tit_list");
        var pdiv = _this.parent("div");
        if (jtitlist.attr("class").indexOf("hide") == -1) {
            return false;
        } else {
            $(this).find(".icon-gt-right").addClass(" icon-gt-down ");
            jtitlist.removeClass("hide");
            pdiv.siblings("div").find(".J_tit_list").removeClass("hide");
            pdiv.siblings("div").find(".icon-gt-right").addClass(" icon-gt-down ");
            pdiv.parent(".floor").siblings(".floor").find(".J_tit_list").addClass(" hide ");
            pdiv.parent(".floor").siblings(".floor").find(".icon-gt-down").removeClass("icon-gt-down");
        }
        $(".J_iscrollbox-tree").each(function () {
            $(this).removeData("iscrollbar").iScrollbar({
                "speed": 50,
                "animH": 253,
                "lineH": 28,
                "listClass": "jstree-container-ul"
            });
        });
    });
    /*已选列表清除全部按钮绑定点击事件*/
    $(".J_tit_list").find(".btn-removeAll").on("click", function (e) {
        var selectedlist = $(this).siblings(".selectedlist").size() > 0 ? $(this).siblings(".selectedlist") : $(this).siblings(".iscroll-selected").find(".selectedlist"); /*增加滚动条div 修改9-23 cjh*/
        var checkboxId = $(this).attr("data-checkboxId");
        var checkboxlist = $("#" + checkboxId);
        if ($.trim(selectedlist.html()) != "") {
            selectedlist.html("");
            checkboxlist.find("[data-checked]").removeClass("checkbox-checked").attr("data-checked", "");
        }
        if (checkboxId == "J_checkboxlist-time") {
            $(".lists-radio").find(":radio[data-checked='true']").attr("checked", false);
        }
        if (checkboxId == "J_checkboxlist-area") {
            $("#J_checkAll").attr("isClick", "");
        }
        /*调用自定义滚动条方法 add 9-23 cjh*/
        autoIscrollbar($(this).siblings(".J_iscroll-selected"), {
            "speed": 50,
            "animH": 391,
            "lineH": 28
        });
    });

    /*.accordion 初始化*/
    Accordion.init($(".accordion"));
    /*底部决策支持分析hover*/
    $("#J_item-jcfx").hover(
      function () {
          $(this).addClass(" hover ");
      },
      function () {
          $(this).removeClass(" hover ");
      }
   );
    /*时间滑块*/
    $('.nstSlider').nstSlider({
        "crossable_handles": false,
        "left_grip_selector": ".leftGrip",
        "right_grip_selector": ".rightGrip",
        "value_bar_selector": ".bar",
        "value_changed_callback": function (cause, leftValue, rightValue) {
            $(this).find(".start").text(leftValue + "年");
            $(this).find(".end").text(rightValue + "年");
            var oselected = leftValue + "年-" + rightValue + "年"
            var orel = leftValue + "-" + rightValue;
            $("#J_selected-time").html('<li ><span class="checkedTxt" rel="' + orel + '">' + orel + '</span></li>');
        }
    });

    /*绑定选择时间 时间滑块与时间段选项点击事件*/
    //时间滑块#J_time_range
    $("#J_time_range").on("focusin", function () {
        /*禁用时间段功能*/
        $("#J_time_block").attr("checked", "");
        $(".lists-radio").find(":radio").each(function () {
            $(this).attr("checked", false);
            $(this).attr("disabled", "disabled");
        });
        Checkbox.destroy("J_checkboxlist-time");
        /*时间滑块重置已选时间*/
        var itext = $(".nstSlider").find(".start").text() + "-" + $(".nstSlider").find(".end").text();
        $("#J_selected-time").html('<li ><span class="checkedTxt" rel="1990-2000">"+itext+"</span></li>');
        /*为滑块解绑mouseUp事件*/
        $(".J_nstSliderbtn").off("mousedown.disabled");
        $('.nstSlider').nstSlider('enable');
        $('.nstSlider').nstSlider('refresh');
    });


    //时间段
    $("#J_time_block").on("focusin", function () {
        $("#J_time_range").attr("checked", "");
        $("#J_selected-time").html("");
        $('.nstSlider').nstSlider('disable');
        $("#J_checkboxlist-time p").find("span").removeClass("checkbox-checked");
        /*为滑块绑定mouseUp事件*/
        //$(".J_nstSliderbtn").on("mousedown.disabled",function(e){
        //  e.stopPropagation();
        //  alert("请先选择：按时间范围选择！");
        //});
        /* 开启选项功能*/
        Checkbox.setEnable("J_checkboxlist-time");
        $(".lists-radio").find(":radio").each(function () {
            $(this).removeAttr("disabled").on("focusin", function () {
                $(this).attr("data-checked", "true");
                var curTxt = $(this).val(),
                    curYear = new Date().getFullYear(),
                    str = "",
                    objs = null;
                var obj = {
                    "近五年": function () {
                        str = createEL(4, curYear-1);
                        str != "" && $("#J_selected-time").html(str);
                        $("#J_checkboxlist-time").find(".checkbox,.btn-icheckAll").removeClass("checkbox-checked").attr("data-checked", "");
                        setCheckedstatus(4, curYear-1);
                    },
                    "近十年": function () {
                        str = createEL(9, curYear-1);
                        str != "" && $("#J_selected-time").html(str);
                        $("#J_checkboxlist-time").find(".checkbox,.btn-icheckAll").removeClass("checkbox-checked").attr("data-checked", ""); ;
                        setCheckedstatus(9, curYear-1);
                    },
                    "2000年以来": function () {
                        str = createEL(15, curYear-1);
                        str != "" && $("#J_selected-time").html(str);
                        $("#J_checkboxlist-time").find(".checkbox,.btn-icheckAll").removeClass("checkbox-checked").attr("data-checked", "");
                        setCheckedstatus(15, curYear-1);
                    }
                };
                obj[curTxt] && obj[curTxt]();
                /*add 9-23 cjh*/
                autoIscrollbar($("#J_selected-time").parent(".J_iscroll-selected"), {
                    "speed": 50,
                    "animH": 391,
                    "lineH": 28
                });
            });
        });

    });
    //$(".lists-radio").on("click",":radio",function(){
    //    $(this).attr("disabled")=="disabled"&&alert("请先选择：按区间快速选择！");
    //});

});
/*---------------------------------------------------------------------------*/
/*时间段*/
function createEL(yearLen,curYear){
  var str="";
   for(var i=curYear-yearLen;i<=curYear;i++){
              str+='<li ><span class="checkedTxt" rel="'+i+'">'+i+'</span><button class="btn btn-del">&times;</button></li>';
   }
   return str;
}

/*时间段#J_checkboxlist-time中对应radio时间范围内的p里的都为勾选状态*/
function setCheckedstatus(yearLen,curYear){
  var ichecksCon=$("#J_checkboxlist-time");
  for(var i=curYear-yearLen;i<=curYear;i++){
      var icheck=ichecksCon.find(".checkbox[rel='"+i+"']");
      var checkAllbtn=icheck.parent("p").find(".btn-icheckAll");
         if(icheck.size()==1){
               icheck.addClass("checkbox-checked").attr("data-checked","true");
               checkAllbtn.attr("class").indexOf("checkbox-checked")==-1&&checkAllbtn.addClass("checkbox-checked").attr("data-checked","true");
         }else{
          ////console.log(".checkbox的rel属性存在重复数据，请去除重复！");
         }
  }
}
/*==============页面交互绑定事件：年度数据分析=========*/
/*年度数据分析中行政区域收起展开收起按钮添加点击事件*/
$("#J_btn-off").on("click",function(){
    var _this=$(this);
    if(_this.text()=="展开"){
          _this.parent().siblings("dd").addClass(" fno ").children(".selectbox").addClass(" arealistbox ");
          _this.text("收起");
    }else if(_this.text()=="收起"){
          _this.parent().siblings("dd").removeClass("fno").children(".selectbox").removeClass("arealistbox");
          _this.text("展开");
    }else{
        return false;
    }
});


/*行政区域选择下级区县全选  全不选 #J_checkAll  J_uncheckAll 绑定点击事件*/
$(".opts").on("click", ".checkopt", function () {
    var oid = $(this).attr("id");
    if ($(this).attr("isClick") == "" || $(this).attr("isClick") == undefined) {
        $(this).attr("isClick", "true");
        var checkbox = $("#J_checkboxlist-area");
        var selectedboxId = $.parseJSON(checkbox.attr("data-setting")).conboxId;
        var checks = checkbox.find(".checkbox");
        if (oid == "J_checkAll") {
            checks.addClass(" checkbox-checked ").attr("data-checked", "true");
            if (selectedboxId != "" && $("#" + selectedboxId).size() == 1) {
                var conbox = $("#" + selectedboxId);
                checks.each(function () {
                    var checkRel = $(this).attr("rel");
                    var checkTxt = $(this).find("span").size() == 0 ? $(this).text() : $(this).find("span").attr("title");
                    if (conbox.find(".checkedTxt[rel='" + checkRel + "']").size() == 0) {
                        var str = "<li><span class='checkedTxt' rel='" + checkRel + "'>" + checkTxt + "</span><button class='btn btn-del'>&times;</button></li>";
                        conbox.html(conbox.html() + str);
                    }
                });
                /*add 9-23 cjh 超出截取省略*/
                conbox.find("span[class='checkedTxt']").each(function () {
                    $(this).find("span").size() == 0 && LIBSTRING.cut($(this), 190);
                });
            }
            $("#J_uncheckAll").attr("isClick", "");
        } else {
            checks.removeClass("checkbox-checked").attr("data-checked", "");
            $("#J_checkAll").attr("isClick", "");
            if (selectedboxId != "" && $("#" + selectedboxId).size() == 1) {
                var conbox = $("#" + selectedboxId);
                checks.each(function () {
                    var checkRel = $(this).attr("rel");
                    var checkTxt = $(this).find("span").size() == 0 ? $(this).text() : $(this).find("span").attr("title");
                    conbox.find(".checkedTxt[rel='" + checkRel + "']").parent("li").remove();
                });
            }
        }
        /*add cjh 9-23 调用自定义滚动条 该处{options}要与Checkbox对象中的一致*/
        autoIscrollbar($("#J_iscroll-selected-a"), {
            "speed": 50,
            "animH": 391,
            "lineH": 28
        });
    } else {
        return false;
    }
    $(this).attr("isClick","");
});

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
    LIBSTRING.fn.cut = function (obj, mwidth, tlen) {
        if (!obj || !obj.length) return;
        tlen < 1 || (tlen = 15);
        $(obj).html(this.cutLen($(obj).html(), parseInt((mwidth || $(obj).width()) / tlen), "..."));
    };
    return LIBSTRING();
})();
/*字符串截取类 end================*/

/*selectbox对象 start  =================*/
;(function($){
  var selfs={};
  var Selectbox=function(sbox){
        this.setting={"showNum":10,"width":198,"url":"www.baidu.com","param":""};
        this.sbox=sbox;
        this.listbox=this.sbox.find(".options");
        this.curTxt=this.sbox.find(".current");
        this.lisNum=this.listbox.find("li").size();
        $.extend(this.setting,this.getSetting());
         if(!!window.ActiveXObject || "ActiveXObject" in window){
            this.resetMinWidth();
         }
        this.bindMainClick();
        this.bindMouseLeave();
        this.bindListliClick();
  };

  Selectbox.prototype={
         /*获取配置参数*/
        getSetting:function(){
             var ds=this.sbox.attr("data-setting");
                 if(ds){
                    return $.parseJSON(ds);
                 }else{
                    return {};
                 }
        },
        /*select主体添加绑定事件*/
        bindMainClick:function(){
            var _this=this;
             _this.sbox.on("click",".current,s",function(){
                    _this.listbox.removeClass("vhide");
                    _this.sbox.addClass(" selectbox-hover ");
               });
        },
        /*绑定鼠标移出selectbox事件*/
        bindMouseLeave:function(){
            var _this=this;
            _this.sbox.on("mouseleave",function(){
               _this.listbox.addClass(" vhide ");
               _this.sbox.removeClass("selectbox-hover");
           });
        },
        /*options下li绑定点击事件*/
        bindListliClick:function(){
            var _this=this;
            _this.sbox.on("click","li",function(){
                var currel=$(this).attr("rel");
                _this.curTxt.html($(this).html()+"<s><\/s>").attr("rel",""+currel+"");
                $(this).addClass("cur").attr("data-selected", "true").siblings("li").attr("data-selected", "").removeClass("cur");
                _this.listbox.scrollTop(0);
                 _this.listbox.addClass(" vhide ");
                 _this.sbox.removeClass("selectbox-hover");
                /*加载异步请求*****************llllllllllll*************************************/
                if (_this.setting.url != "") {
                    ////console.log("加载异步请求开始");
                    if($(this).parent().parent().attr("id")=="J_areaTypelist"){
                        _this.setting.param={ ZoneType:currel };
                    }
                    else{
                        _this.setting.param={ XjCode:currel };
                    }
                    var data = _this.load(_this.setting.url, _this.setting.param);
                    data && _this.writeHtml(data);
                }
               });
        },
        /*如果是ie浏览器 重新设置options的min-width值*/
        resetMinWidth:function(){
           var owidth=this.listbox.width();
           var pwidth=this.sbox.width();
           /*判断是否出现滚动条*/
           if(this.lisNum>this.setting.showNum){
              this.listbox.css({"minWidth":this.setting.width-19});
           }
           if(this.lisNum<this.setting.showNum&&navigator.appName == "Microsoft Internet Explorer" && navigator.appVersion .split(";")[1].replace(/[ ]/g,"")=="MSIE7.0"){
                 var w=getMaxWidth(this.listbox,this.setting.width);
                   if(w>=this.setting.width){
                      this.listbox.find("li").width(w);
                      this.listbox.width(w+10);
                    }else{
                      this.listbox.css({"width":this.setting.width-19});
                    }   
                }
           
        },
        /*联动数据加载*/
        load:function(url,param){
             ////console.log("==========load");
             //return "返回加载完成的数据";
            $.post(url,param,function(data){
                $("#J_checkboxlist-area").html("");
                $.each(data,function(k,v){
                    $("#J_checkboxlist-area").append("<span rel=\""+v.XjCode+";"+v.ZoneCode+";"+v.ZoneName+"\" class=\"checkbox\">"+v.ZoneName+"</span>");
                });
                if(param.XjCode){ ;
                    if(param.XjCode.length<=4){
                        $("#J_subArealist").find("ul").html("");
                        $("#J_subArealist").find(".current").attr("rel", data[0].XjCode);
                        $("#J_subArealist").find(".current").html(data[0].ZoneName + "<s></s>"); 
                        $.each(data,function(k,v){
                           $("#J_subArealist").find("ul").append("<li rel=\"" + v.XjCode + "\">" + v.ZoneName + "</li>");
                        });
                    }
                }
                if(param.ZoneType){
                    $("#J_subArealist").find("ul").html("");
                    $("#J_subArealist").find(".current").attr("rel", data[0].XjCode);
                    $("#J_subArealist").find(".current").html(data[0].ZoneName + "<s></s>"); 
                    $.each(data,function(k,v){
                        $("#J_subArealist").find("ul").append("<li rel=\"" + v.XjCode + "\">" + v.ZoneName + "</li>");
                    });
                }
                $("#J_checkboxlist-area").find(".checkbox").each(function(){
                     LIBSTRING.cut($(this),100);
                });
                  $($("#J_areachecklist").find(".J_iscrollbox")[0]).removeData("iscrollbar").iScrollbar({
                     "speed":50,
                     "animH":161,
                     "lineH":23
                  });
            });
        },
        /*局部刷新页面数据处理*/
        writeHtml:function(data){
             ////console.log("writeHtml=========");
        }
  };

  Selectbox.init=function(sboxs){
        var _this=this;
        sboxs.each(function(){
          var sboxId=$(this).attr("id");
            selfs[""+sboxId+""]=new _this($(this));
        });
  };

  Selectbox.destroy=function(selectboxId){
       if($.trim(selectboxId)!=""&&$("#"+selectboxId).size()==1){
           selfs[""+selectboxId+""]=null;
       }
  }

  Selectbox.loadData=function(url,param,selectboxId){
    if($.trim(selectboxId)!=""&&$("#"+selectboxId).size()==1&&$.trim(url)!=""){
      return  selfs[""+selectboxId+""].load(url,param);
    }
        
  }
  window["Selectbox"]=Selectbox;
})(jQuery);
/*selectbox对象 end=================*/

/*Checkbox对象 使用到了字符串截取类======================*/
;(function($){
   var selfs={};
   var Checkbox=function(check){
          this.setting={"len":147,       //checkbox中文超出省略显示的参数 默认六个汉字
                                "len1":"190",//已选择列表默认超出省略参数  修改由210变为190 update9-23cjh
                               "conboxId":"",//盛放被选中内容的容器ID
                               "disabled":"false",//是否可点选 默认为false可点选
                               "checkAllClass":"btn-icheckAll"//全选按钮class
                              };
          this.check=check;
          this.checkAllbtn=check.find("."+this.setting.checkAllClass);
          this.checkboxs=check.find(".checkbox");
          $.extend(this.setting,this.getSetting());
          this.conbox=$("#"+this.setting.conboxId);
             /*设置超出省略*/
             this.setOverflow();
             /*绑定点击事件*/
             this.bindClick();
          if(this.setting.disabled=="true"){
                this.disabled();
                this.checkAllbtn.addClass(" check-disabled ");
          }else{
              if(this.setting.checkAllClass&&this.checkAllbtn.size()>0){
                this.bindCheckAllBtn();
                this.checkAllbtn.removeClass(" check-disabled ");
              }
          }
         
   };
   Checkbox.prototype={
    /*获取配置参数*/
        getSetting:function(){
             var ds=this.check.attr("data-setting");
                 if(ds){
                    return $.parseJSON(ds);
                 }else{
                    return {};
                 }
        },
        /*设置超出省略*/
       setOverflow:function(){
        var _this=this;
        _this.check.find(".checkbox").each(function(){
           LIBSTRING.cut($(this),_this.setting["len"]);
        });
       },
       /*绑定点击事件*/
       bindClick:function(){
        var _this=this;
         this.check.on("click.icheck",".checkbox",function(){
         
                if($(this).attr("data-checked")=="true"){
                $(this).removeClass("checkbox-checked").attr("data-checked","");
                _this.removeChecked($(this));
                $("#J_checkAll")&&$("#J_checkAll").attr("isClick","");
                if(_this.checkAllbtn.size()>0){
                  if(_this.check.find(".checkbox[data-checked='true'][rel^=2]").size()==0){
                    $(".lists-radio").find(":radio[data-checked='true']").attr("checked",false);
                  }
                  $(this).siblings(".checkbox[data-checked='true']").size()==0&&$(this).siblings(".btn-icheckAll").removeClass("checkbox-checked").attr("data-checked","");
                }
                }else{
                $(this).addClass(" checkbox-checked ").attr("data-checked","true");
                $("#J_uncheckAll")&&$("#J_uncheckAll").attr("isClick","");
                if(_this.checkAllbtn.size()>0&&$(this).siblings("."+_this.setting.checkAllClass).attr("class").indexOf("checked")==-1){
                       $(this).siblings("."+_this.setting.checkAllClass).addClass(" checkbox-checked ").attr("data-checked","true");
                }
                _this.addcheckeds($(this));
                }
            
         });
       },
    /*将已选checkbox中的内容添加到指定标签中*/
    addcheckeds:function(checkitem){
        var _this=this;
        var conId=this.setting["conboxId"];
        var  conbox=$("#"+conId+"");
        var checkRel=checkitem.attr("rel");
        var extend=checkitem.attr("extend");
        var  checkTxt=checkitem.find("span").size()==0?checkitem.text():checkitem.find("span").attr("title");
        var  flag=conbox.find(".checkedTxt[rel='"+checkRel+"']").size();
            if(conId!=""&&conbox.size()==1&&flag==0){
                var str="";
                if(extend)
                {
                str="<li><span class='checkedTxt' rel='"+checkRel+"' extend='"+extend+"'>"+checkTxt+"</span><button class='btn btn-del'>&times;</button></li>";
                }
                else
                {
                    str="<li><span class='checkedTxt' rel='"+checkRel+"'>"+checkTxt+"</span><button class='btn btn-del'>&times;</button></li>";
                }
                conbox.html(conbox.html()+str);
                this.exeIscroll(this.setting["conboxId"]);/*add 9-23 cjh*/
            }
            conbox.find("span[rel='"+checkRel+"']").each(function(){
                 $(this).find("span").size()==0&&LIBSTRING.cut($(this),_this.setting["len1"]);
            });
           
        },
        /*移除已添加的checkbox内容*/
        removeChecked:function(checkitem){
             if(this.setting.conboxId!=""){
                    var  conbox=$("#"+this.setting.conboxId+"");
                    var checkRel=checkitem.attr("rel");
                    var  checkTxt=checkitem.find("span").size()==0?checkitem.text():checkitem.find("span").attr("title");
                    if(conbox.size()==1){
                       conbox.find(".checkedTxt[rel='"+checkRel+"']").parent("li").remove();
                    }
                      this.exeIscroll(this.setting["conboxId"]);/*add 9-23 cjh*/
             }
        },
         /*checkbox disabled*/
      disabled:function(opt){
            //移除.checkbox 的click事件
            this.check.off("click.icheck",".checkbox");
            this.check.on("click.disabled",".checkbox,.btn-icheckAll",function(){
                  alert("请先选择：按区间快速选择！");
            });
            this.checkboxs.each(function(){
                   var $this=$(this);
                   $this.addClass(" check-disabled ");
                  if($this.attr("class").indexOf("checked")>-1){
                    $this.removeClass("checkbox-checked");
                  }
               });
         this.checkAllbtn.size()>0&&this.offCheckAllBtn();
        },
        /*全选或全不选按钮 绑定事件 */
        bindCheckAllBtn:function(){
          var _this=this;
          _this.checkAllbtn.removeClass("check-disabled");
          this.checkAllbtn.on("click.checkall",function(){
                 var  checks=$(this).siblings(".checkbox");
                 if($(this).attr("data-checked")==undefined||$(this).attr("data-checked")==""){
                       $(this).addClass("checkbox-checked").attr("data-checked","true");
                       checks.addClass("checkbox-checked").attr("data-checked","true");
                       checks.each(function(){
                         _this.addcheckeds($(this));
                       });
                 }else{
                       $(this).removeClass("checkbox-checked").attr("data-checked","");
                       checks.removeClass("checkbox-checked").attr("data-checked","");
                       checks.each(function(){
                         _this.removeChecked($(this));
                       });
                        if(_this.check.find(".checkbox[data-checked='true'][rel^=2]").size()==0){
                        $(".lists-radio").find(":radio[data-checked='true']").attr("checked",false);
                      }
                 }
           });
        },
        /*全选或全不选按钮 取消绑定事件 */
        offCheckAllBtn:function(){
          var _this=this;
          _this.checkAllbtn.off("click.checkall");
          _this.checkAllbtn.each(function(){
            $(this).addClass(" check-disabled ");
             if($(this).attr("class").indexOf("checked")>-1){
                    $(this).removeClass("checkbox-checked");
             }
             
          });
        },
        /*自定义滚动条方法调用*/
        exeIscroll:function(conboxId){
           /*已选指标选择列表 autoIscrollbar为public.js中的公共方法*/
           autoIscrollbar($("#"+conboxId).parent(".J_iscroll-selected"),{
                 "speed":50,
                 "animH":391,
                 "lineH":28
              });
        }

    }

   /*checkbox初始化*/
  Checkbox.init=function(checks){
       var _this=this;
       checks.each(function(){
        var key=$(this).attr("id");
        if(selfs[key]==undefined||selfs[key]==null){
           selfs[key]=new _this($(this));
        }
       });
  }

         /*checkbox enable*/
      Checkbox.setEnable=function(checkboxId){
        if(checkboxId!=""&&selfs[checkboxId]){
            var _this= selfs[checkboxId];
            _this.checkboxs.each(function(){
                  $(this).removeClass("check-disabled").removeClass("check-checked-disabled").attr("data-checked","");
            });
              _this.bindClick();
              if(_this.checkAllbtn.size()>0){
                _this.check.off("click.disabled");
                _this.bindCheckAllBtn();
              }
              
          }else{
         //console.log("Checkbox的方法setEnable的传入参数不正确！或"+checkboxId+"未进行初始化！");
        }  
      }

   /* checkbox销毁*/
   Checkbox.destroy=function(checkboxId){
          selfs[checkboxId].disabled();
   }

   window["Checkbox"]=Checkbox;
})(jQuery);
/*Checkbox对象 end ======================*/

/*年度数据分析中的map对象 start===========*/
;(function($){
    var Map=function(map){
          this.setting={"bigMpId":"J_bigMap","optId":"J_mapoptbox"};
          this.map=map;
          $.extend(this.setting,this.getSetting());
          this.bigMap=$("#"+this.setting.bigMpId);
          this.optbox=$("#"+this.setting.optId);
          //this.bindsmallClick();
          //this.bindbigClick();
          this.changeMaplevel();
    };

    Map.prototype={
        /*获取外部设置的参数*/
         getSetting:function(){
            var settings=this.map.attr("data-setting");
           if(settings&&settings!=""){
               return $.parseJSON(settings);
           }else{
               return {};
           }
         },
         /*小地图绑定点击事件*/
         bindsmallClick:function(){
            var _this=this;
            _this.map.on("click",".btn-scale,img",function(){
              $("#"+_this.setting.bigMpId).removeClass("vhide");
            });
         },
         /*大地图绑定点击事件*/
         bindbigClick:function(){
            var _this=this;
            _this.bigMap.on("click",".btn-scale",function(){
                   _this.bigMap.addClass(" vhide ");
            });
        },
        /*省、市、县切换*/
        changeMaplevel:function(){
             //为轴、文字添加点击事件 
             var _this=this;
             _this.optbox.on("click",".item,s",function(){
                var ovalue=null;
                if($(this).siblings(".maptip")&&$(this).siblings(".maptip").size()==1){
                    var p=$(this).parent();
                     ovalue=$.trim(p.attr("class").replace("item",""));
                     $(this).siblings(".maptip").removeClass("vhide");
                     p.siblings(".item").find(".maptip").addClass("vhide");
                }else{
                    ovalue=$.trim($(this).attr("class").replace("item",""));
                    $(this).find(".maptip").removeClass("vhide")
                    $(this).siblings(".item").find(".maptip").addClass("vhide");
                }
                $("#J_mp").attr("data-status",ovalue);
             })
             //＋ 一绑定点击事件        
             $(".btn-moveUp").on("click",function(e){
                e.stopPropagation();  
                var curLevel=$("#J_mp").attr("data-status");
                ////console.log("===========curLevel"+curLevel);
                var obj={"province":function(){
                                  var city=_this.optbox.find(".city");
                                        city.find(".maptip").removeClass("vhide");
                                        city.siblings(".item").find(".maptip").addClass("vhide");
                                        $("#J_mp").attr("data-status","city");
                                   },
                              "city":function(){
                                   var county=_this.optbox.find(".county");
                                        county.find(".maptip").removeClass("vhide");
                                        county.siblings(".item").find(".maptip").addClass("vhide");
                                        $("#J_mp").attr("data-status","county");
                                   },
                              "county":function(){
                                        return false;
                                   }
                             };
                  obj[curLevel]&&obj[curLevel]();
             })

            $(".btn-moveDn").on("click",function(e){
                e.stopPropagation();  
                var curLevel=$("#J_mp").attr("data-status");
                var obj={"province":function(){
                                  return false;
                                   },
                              "city":function(){
                                   var province=_this.optbox.find(".province");
                                        province.find(".maptip").removeClass("vhide");
                                        province.siblings(".item").find(".maptip").addClass("vhide");
                                        $("#J_mp").attr("data-status","province");
                                   },
                              "county":function(){
                                       var city=_this.optbox.find(".city");
                                        city.find(".maptip").removeClass("vhide");
                                        city.siblings(".item").find(".maptip").addClass("vhide");
                                        $("#J_mp").attr("data-status","city");
                                   }
                             };
                  obj[curLevel]&&obj[curLevel]();
             })
        }
    };

    Map.init=function(map){
        var _this=this;
        new _this(map);
    }
    window["Map"]=Map;
})(jQuery);
/*map对象 end==========*/

/*Accordion对象 start=============*/
;(function($){
  var Accordion=function(ad){
    this.ad=ad;
    this.bindClick();
  };
  Accordion.prototype={
       bindClick:function(){
        var _this=this;
            _this.ad.on("click",".adtit",function(){
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
    Accordion.init=function(ads){
        var _this=this;
        ads.each(function(){
           new _this($(this));
        });
    }
    window["Accordion"]=Accordion;
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