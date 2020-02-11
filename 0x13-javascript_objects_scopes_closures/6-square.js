#!/usr/bin/node

const fiveSquareDotJs = require('./5-square');

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

module.exports = Square;
