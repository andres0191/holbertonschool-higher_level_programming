#!/usr/bin/node
const fs = require('fs');
const dir = process.argv[2];
const tex = process.argv[3];
fs.writeFile(dir, tex, function (err) {
  if (err) {
    return console.log(err);
  }
});
