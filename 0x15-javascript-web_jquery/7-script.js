#!/usr/bin/node
/* Write a Javascript script that fetches and replaces the name of this URL: https://swapi-api.hbtn.io/api/people/5/?format=json */
/* how to realized a get petition link: https://api.jquery.com/jQuery.get/ */
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('#character').text(data.name);
});
