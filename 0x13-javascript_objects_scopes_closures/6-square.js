#!/usr/bin/node
/* Write a class Rectangle that defines a rectangle */
const Squaretask5 = require('./5-Square.js');
class Square extends Squaretask5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = 0;
    for (i = 0; i <= this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
