#!/usr/bin/node
function addition (x, y) {
  return (x + y);
}
console.log(addition(Number(process.argv[2]), Number(process.argv[3])));
