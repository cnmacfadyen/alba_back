// We were having some issues with the CSRF cookies, but found this link to be very helpful
// https://docs.djangoproject.com/en/2.1/ref/csrf/


var csrf = getCookie('csrftoken')

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain){
            xhr.setRequestHeader("X-CSRFToken", csrf)
        }
    }
});

function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$("#review_form").on('submit', function(event){
   event.preventDefault();
   console.log("form submitted");
   if ( $("#No_comments").length ) {
       $("#No_comments").hide();
   }
   create_review();
});


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function create_review(){
  $.ajax({
      url: "",
      type: "POST",
      dataType: "JSON",
      data: { "comment" : $('#id_comment').val()},
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