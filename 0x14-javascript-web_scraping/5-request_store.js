#!/usr/bin/node
/* Write a script that gets the contents of a webpage and stores it in a file */
const request = require('request');
const fs = require('fs'); const url = process.argv[2]; const name = process.argv[3];
request.get(url).on('error', function (error) {
  if (error) {
    console.log(error);
  }
}).pipe(fs.createWriteStream(name, 'utf-8'));
