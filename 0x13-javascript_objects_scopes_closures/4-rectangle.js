#!/usr/bin/node
/* Write a class Rectangle that defines a rectangle */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
    } else if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
};
