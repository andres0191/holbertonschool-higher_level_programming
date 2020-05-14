#!/usr/bin/node
/* Write a script that computes the number of tasks completed by user id. */
const request = require('request'); const url = process.argv[2] + '?completed=true'; const obj = Object();
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } const json = JSON.parse(body);
  for (const job of json) {
    if (Object.prototype.hasOwnProperty.call(obj, job.userId)) {
      obj[job.userId]++;
    } else {
      obj[job.userId] = 1;
    }
  }
  console.log(obj);
});
