$(function(){
    /*首页侧边栏导航 子菜单字符串截取*/
    $("#J_sideNav").find(".itemTxt").each(function(){
         LIBSTRING.cut($(this),150);
    });
    $("#J_sideNav").find(".item").hover(function(){
       var index=$("#J_sideNav").find(".item").index($(this));
       var subNav=$(this).find(".subnav");
       var otop=subNav.position().top-index*$(this).outerHeight(true);
             subNav.css({
                top:otop+"px"
             });
        $(this).addClass(" hover ");
    },function(){
        $(this).removeClass("hover");
        var subNav=$(this).find(".subnav");
        subNav.css({
                top:"0"
             });
    });
    /*数据分析 右侧小图片绑定mouseenter 事件*/
     var  J_da_picBig=$("#J_da_picBig");
    $("#J_da_piclist").on("mouseenter","a[data-setting]",function(){
        try{
            var _this=$(this);
                  odataSetting=_this.attr("data-setting");
            if($.trim(odataSetting)!=""&&odataSetting){
                var settings=$.parseJSON(odataSetting);
                $.extend({},settings);
                J_da_picBig.find("img").attr("src",settings.bigSrc);
                J_da_picBig.find(".btn-link").text(settings.btnText).attr("href",settings.btnHref);
            }else{
                return false;
            }
        }catch(err){
           //console.log("数据分析#J_da_piclist的mouseenter事件异常："+err.message);
           return false;
        }
    });
        /*最近更新 名称超长截取 */
    $("#J_laster").find(".mod-l .J_name").each(function(){
         LIBSTRING.cut($(this),290);
    });    
    $("#J_laster").find(".mod-r .J_name").each(function(){
         LIBSTRING.cut($(this),380);
    });

    /*设置placeholder */
    setPlaceHolder($(".fpacehd"));
    /*课题研究 标题超长截取*/
    $("#J_researchList").find(".J_retit").each(function(){
      LIBSTRING.cut($(this),440);
    });
});
$(window).load(function(){
  $("#J_nivoSlider").nivoSlider({
    effect:"fade",
    animSpeed:500,
    pauseTime:2500,
    startSlide:0, 
    directionNav:false,
    controlNav:true,
    controlNavThumbs:false,
    pauseOnHover:true
  });
});