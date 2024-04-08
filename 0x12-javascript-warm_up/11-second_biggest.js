#!/usr/bin/node

const len = process.argv.length;
let counter = 2;
const new_array = [];

if (process.argv[2] || process.argv[3] === undefined) {
  console.log('0');
} else {
  while (counter < len) {
    new_array.push(process.argv[counter])
    counter++;
  }
  num = new_array.sort((a, b) => b - a)
  console.log(num[1])
}
