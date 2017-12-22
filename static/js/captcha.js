$(function(){
    $.get("/captcha/refresh/?"+Math.random(), function(result){
            $("#id_captcha_1").val('');
            $('.captcha').attr("src",result.image_url);
            $('#id_captcha_0').attr("value",result.key);
        });
});

//刷新验证码
$(".captcha").bind("click",function(){
    $.get("/captcha/refresh/?"+Math.random(), function(result){
            $("#id_captcha_1").val('').focus();
            $('.captcha').attr("src",result.image_url);
            $('#id_captcha_0').attr("value",result.key);
        });
});