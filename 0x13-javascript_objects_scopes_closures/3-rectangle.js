#!/usr/bin/node
/* Write a class Rectangle that defines a rectangle*/
class Rectangle {
    constructor(w, h){
    if (w <= 0 || h <= 0){
    }else if(w > 0 && h > 0){
        this.width = w;
        this.height = h;
        }
    }
print() {
    let i = 0, j = 0, result = '';
    for(i = 0; i < this.height; i++){
        console.log('X'.repeat(this.width));
        }
        }
}
module.exports = Rectangle;