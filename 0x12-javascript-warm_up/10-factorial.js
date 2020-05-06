#!/usr/bin/node
/*script that computes and prints a factorial*/
const a = parseInt(process.argv[2]);
function factorial (a) {
 return (a != 1) ? a * factorial(a - 1) : 1;
}
if (process.argv[2] == undefined || process.argv[2] == 0) {
  console.log('1');
} else {
  console.log(factorial(a));
}
