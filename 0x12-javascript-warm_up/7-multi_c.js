#!/usr/bin/node
/* script that prints x times C is fun */
let i = 0;
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} for (i = 0; i < parseInt(process.argv[2]); i++) {
  console.log('C is fun');
}
