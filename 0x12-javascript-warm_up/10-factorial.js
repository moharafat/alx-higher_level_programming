#!/usr/bin/node
const Number = parseInt(process.argv[2]);
let fact;

function factorial (Number) {
  if (Number === 0) {
    return 1;
  }
  return (Number * factorial(Number - 1));
}
if (isNaN(Number)) {
  console.log('1');
} else {
  fact = factorial(Number);
  console.log(fact);
}
