$(document).ready(function() {
  // var form = $('#form');
  // var submit = $('#submit');

  $('#submit').on('click', function(e)) {
    e.preventDefault();
  })
});




$("#review_form").on('submit', function(event){
   event.preventDefault();
   console.log("form submitted");
   if ( $("#No_comments").length ) {
       $("#No_comments").hide();
   }
   create_review();
});




function create_review(){
  $.ajax({
      url: "",
      type: "POST",
      dataType: "JSON",
      data: { "comment" : $('#id_comment').val();
      success: function(json){
         $('#id_comment').val('');
         console.log(json);
         location.reload();
         $('.comment_section').prepend("<p>" + json.comment + "</p><p style='color:#2e9fb5;'><strong> - " + json.user + "</strong></p><p style=\"color:#C7C6CB; font-size: medium\"><i>" + json.date + "</i></p>");
      },
      error: function(xhr, errmsg, err){
          console.log(xhr.status + ": " + xhr.responseText);
      }
  });
};