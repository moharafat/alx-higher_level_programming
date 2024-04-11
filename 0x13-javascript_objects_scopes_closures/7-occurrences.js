#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let NumberOfOccurences = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) NumberOfOccurences++;
  }
  return NumberOfOccurences;
};
