#!/usr/bin/node
/* Write a Javascript script that toggles the class of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#toggle_header */

/* toggleClass is for One or more classes (separated by spaces) to be toggled for each element in the matched set. link: https://api.jquery.com/toggleclass/ */
$('#toggle_header').click(function () {
  $('header').toggleClass('red green');
});
