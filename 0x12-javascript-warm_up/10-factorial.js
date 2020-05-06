#!/usr/bin/node
/* script that computes and prints a factorial */
const a = process.argv[2];
function factorial (a) {
  if (isNaN(a) || a === undefined || a < 1) {
    return 1;
  } return ((a !== 1) ? a * factorial(a - 1) : 1);
}
console.log(factorial(a));
