#!/usr/bin/node
/* write a script that display the status code of a GET request8 */
const request = require('request');
request(process.argv[2], function (error, response) {
  console.error('error:', error);
  console.log('statusCode:', response && response.statusCode);
});
