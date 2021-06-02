function respNav() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }

$(".scrollTo").on('click', function(e) {
  e.preventDefault();
  var target = $(this).attr('href');
  $('html, body').animate({
    scrollTop: ($(target).offset().top)
  }, 2000);
});