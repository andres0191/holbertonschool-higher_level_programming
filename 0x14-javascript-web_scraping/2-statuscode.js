#!/usr/bin/node
/* write a script that display the status code of a GET request8 */
const https = require('https');
const url = process.argv[2];
https.get(url, function (res) {
  console.log('code:', res.statusCode);
});
