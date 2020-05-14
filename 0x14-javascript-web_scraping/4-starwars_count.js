#!/usr/bin/node
/* Write ascript that print the number of movies where the character Wedge Antilles is present */
const request = require('request'); const url = process.argv[2]; const movie =0;
request.get(url, function (error, body) {
  if (error) {
    console.log(error);
  } let i = 0; let name; let movie = 0;
    for movie of JSON.parse(body).data){
      for (name of movie.characters) {
        if (name.search('/18/')) {
          i++;
        }
      }
      console.log(i);
    }
};
