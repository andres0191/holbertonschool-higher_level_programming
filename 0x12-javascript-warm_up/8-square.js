#!/usr/bin/node
/* Write a script that prints a square */
let i = 0;
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
