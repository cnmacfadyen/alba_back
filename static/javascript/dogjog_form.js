$("#review_form").on('submit', function(event){
	event.preventDefault();
	console.log("form submitted");
	if ($("#No_comments).length"){
		$("#No_comments").hide();
	}
	create_review();
});


function create_review(){
	$.ajax{{
		url: "",
		type:"POST",
		dataType:"JSON",
		data: {"comment" : $('#id_comment').val(), "rating":
	$('#id_rating').val()},
		success.function(json){
		$('#id_comment').val('')
	}}
}