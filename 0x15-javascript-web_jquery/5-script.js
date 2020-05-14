#!/usr/bin/node
/* Write a Javascript script that adds a LI element to a list when the user clicks on the tag DIV#add_item */
/* You can create content and insert it into several elements at once linkn https://api.jquery.com/append/ */
$('#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
