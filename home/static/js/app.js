$(document).ready(function(){
  $("#search").on("keyup", function(){
    var value = $(this).val().toLowerCase();
    $(".card-title").filter(function(){
      $(this).parents(".card").toggle($(this).text().toLowerCase().indexOf(value) > -1);
    })
  });

  $(".post-like").hover(function(){
    $(this).children().text("favorite")
  }, function(){
    $(this).children().text("favorite_border")
  })
});