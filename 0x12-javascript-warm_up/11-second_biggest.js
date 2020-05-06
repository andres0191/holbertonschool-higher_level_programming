#!/usr/bin/node
/* script that searches the second biggest
integer in the list of arguments */
const a = process.argv.length;
if (a > 3) {
  console.log(process.argv.sort().reverse()[1]);
} else {
  console.log('0');
}
