#!/usr/bin/node
/* Write a class Rectangle that defines a rectangle*/
class Rectangle {
    constructor(w, h){
    if (w <= 0 || h <= 0){
    }else if(w > 0 && h > 0){
        this.widht = w;
        this.height = h;
        }
    }
}
module.exports = Rectangle;
