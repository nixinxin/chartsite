
$("#labBtn").click(function(){location.href="/share/"});
$(function(){
    if($.cookie('Token')){
        $.get('/users/', function(data, status){
            if(status==='200'){

            }
        })
    }
})