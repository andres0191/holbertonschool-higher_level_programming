#!/usr/bin/node
/* Write a Javascript script that updates the text of the HTML tag HEADER to New Header!!!, link https://www.w3schools.com/jquery/html_text.asp */

$('#update_header').click(function () {
  $('header').text('New Header!!!');
});
