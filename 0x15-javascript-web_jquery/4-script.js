// updates the text color of the HTML tag HEADER to red (#FF0000)
// when the user clicks on the tag DIV#red_header with jQuery API

$('DIV#toggle_header').click(function () {
  $('header').toggleClass('red green');
});
