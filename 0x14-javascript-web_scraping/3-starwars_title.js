#!/usr/bin/node
/* Write a script that prints the title of a Star Wars movie where the episode number matches a given integer. */
const request = require('request');
const myurl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(myurl + '/', function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
