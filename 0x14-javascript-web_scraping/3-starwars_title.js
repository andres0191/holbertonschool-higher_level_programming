#!/usr/bin/node
/* Write a script that prints the title of a Star Wars*/
let request = require('request');
let myurl = 'https://swapi-api.hbtn.io/api/films/:'
request.get(myurl + process.argv[2] + '/', function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
