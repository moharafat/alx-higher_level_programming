#!/usr/bin/node
const myVar = process.argv[2];
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
}
for (let row = 0; row < myVar; row++) {
    console.log('X');
}
