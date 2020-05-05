#!/usr/bin/node
/* script that prints two arguments passed
to it, in the following format */
if (process.argv[2] === undefined) {
  console.log('undefined is undefined');
} else if (process.argv[2] === 'c' && process.argv[3] === 'cool') {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else if (process.argv[2] === 'c' && process.argv[3] === undefined) {
  console.log(process.argv[2] + ' is undefined');
}
