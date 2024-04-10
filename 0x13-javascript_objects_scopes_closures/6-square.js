#!/usr/bin/node
const SquareOld = require('./5-square');
class Square extends SquareOld {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    if (c === undefined);
    for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
  }
}
module.exports = Square;
