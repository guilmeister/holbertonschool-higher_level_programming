#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w === 0 || w < 0 || h === 0 || h < 0 || isNaN(w) || isNaN(h)) {

    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const string = 'X';
    let x = 0;
    for (; x < this.height; x++) {
      console.log(string.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
