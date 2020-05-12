#!/usr/bin/node
/* Write a script that prints the title of a Star Wars movie where the episode number matches a given integer. */
let request = require('request');
request.get('http://swapi.co/api/films/' + process.argv[2] + '/', function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
