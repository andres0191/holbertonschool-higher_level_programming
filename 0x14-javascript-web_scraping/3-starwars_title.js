#!/usr/bin/node
/* Write a script that prints the title of a Star Wars movie where the episode number matches a given integer. */
const request = require('request');
const data = process.argv[2];
const myurl = 'http://swapi.co/api/films/';

request.get(myurl + data + '/', function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
