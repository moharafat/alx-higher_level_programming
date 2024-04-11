#!/usr/bin/node
let NumberOfArguments = 0;
exports.logMe = function (item) {
  console.log(NumberOfArguments + ': ' + item);
  NumberOfArguments++;
};
