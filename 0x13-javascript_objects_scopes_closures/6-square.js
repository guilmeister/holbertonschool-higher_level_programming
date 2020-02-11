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

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

const fiveSquareDotJs = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};

class Square extends fiveSquareDotJs {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let x = 0;
    for (; x < this.height; x++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
module.exports = Square;
