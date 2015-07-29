$(document).ready(function(){
	// autocomplete for user assginee
	$(function() {
			$("#user-suggest").autocomplete({
			  source: '/get-users/'
			});
		
	  });
});