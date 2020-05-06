#!/usr/bin/node
/* Write a script that prints a square */
let i = 0;
if (Number.isNaN(parseInt(process.argv[2] === undefined))) {
  console.log('Missing size');
} for (i = 0; i < parseInt(process.argv[2]); i++) {
  console.log('x'.repeat(parseInt(process.argv[2])));
}
