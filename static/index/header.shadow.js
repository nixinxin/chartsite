+function($){
  $.fn.autoShadow = function(options){
    var defaults = {};
    var opts = $.extend(defaults,options);
    return this.each(function(){
      var el = this;
      $(window).scroll(function(){
        var top = document.body.scrollTop;
        if(top <= 0 && $(el).hasClass("docs-nav-shadow")){
          $(el).removeClass("docs-nav-shadow");
        }
        if(top > 0 && !($(el).hasClass("docs-nav-shadow"))){
          $(el).addClass("docs-nav-shadow");
        }
      })
    });
  };
  //init
  $(function(){
    $(".docs-nav").autoShadow();
  });
}(jQuery);