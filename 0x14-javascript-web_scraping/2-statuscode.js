#!/usr/bin/node
/* write a script that display the status code of a GET request8 */
const request = require('request');
const myurl = process.argv[2];
request(myurl, function (response) {
  console.log('code:', response.statusCode);
});
