$(function() {
    $('.video-tile').matchHeight();
  	$('.video-tile').each(function(i) {
  		var videoTile = $(this);
	    setTimeout(function() {
	    	videoTile.addClass('loaded');
	    }, i*100); // delay 100 ms
  	});
});