#!/usr/bin/node
/* Write a script that prints a message depending
of the number of arguments passed */
if (process.argv[2] === undefined) {
  console.log('No argument');
} else if (process.argv[3]) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
