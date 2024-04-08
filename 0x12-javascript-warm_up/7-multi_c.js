#!/usr/bin/node
const myVar = process.argv[2];
let count = 0;
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
}
while (count < myVar) {
  console.log('C is fun');
  count++;
}
