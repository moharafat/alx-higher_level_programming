#!/usr/bin/node
const len = process.argv.length;
if (len <= 2) {
  console.log('No argument');
}
if (len > 2) {
  console.log('Argument found');
}