#!/usr/bin/node
/* Write a script that prints the title of a Star Wars movie where the episode number matches a given integer. */
const request = require('request');
const number = process.argv[2];
const myurl = 'https://swapi-api.hbtn.io/api/films/' + number;
request.get(myurl, function (error, response, body) {
  if (error) {
    console.log(error);
  } console.log(JSON.parse(body).title);
});
