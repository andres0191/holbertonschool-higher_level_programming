#!/usr/bin/node
/* script that computes and prints a factorial */
const a = parseInt(process.argv[2]);
function factorial (a) {
  if (isNaN(a) || process.argv[2] === undefined || process.argv[2] == 0) {
    return 1;
  } return ((a !== 1) ? a * factorial(a - 1) : 1);
}
console.log(factorial(a));
