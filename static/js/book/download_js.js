// JavaScript Document
$(document).ready(function() {
    $('.download_ul').click(function(){
		$('.download').toggle()
		})
	 $('.download_ul').hover(function(){},
	 function(){
		$('.download').hide() 
	 })
});