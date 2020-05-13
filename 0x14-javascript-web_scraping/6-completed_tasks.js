#!/usr/bin/node
/* Write a script that computes the number of tasks completed by user id.*/
const request = require('request'); const url = process.argv[2]+'?completed=true'; const i = 0;
request.get(url, function (error, response, body) {
   if (error){
console.log(error);
} for(i of JSON.parse(body)){
if (i.completed === true){
}

});
