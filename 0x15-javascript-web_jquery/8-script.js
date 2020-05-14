#!/usr/bin/node
/* Write a Javascript script that fetches and lists all movies title by using this URL: https://swapi-api.hbtn.io/api/films/?format=json */
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const film of data.results) {
    $('ul#list_movies').append($('<li></li>').text(film.title));
  }
});
