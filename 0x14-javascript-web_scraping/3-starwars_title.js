#!/usr/bin/node
/* Write a script that prints the title of a Star Wars*/
let request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/:' + process.argv[2] + '/', function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
