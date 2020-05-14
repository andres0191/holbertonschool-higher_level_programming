#!/usr/bin/node
/* Write a Javascript script that adds the class red to the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header */
/* More than one class may be added at a time, separated by a space, to the set of matched elements link: https://api.jquery.com/addClass/https://api.jquery.com/addClass/ */
$('#red_header').click(function () {
  $('header').addClass('red');
});
