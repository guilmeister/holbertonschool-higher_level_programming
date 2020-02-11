#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  let counter = 0;
  for (; x < list.length; x++) {
    if (list[x] === searchElement) {
      counter = counter + 1;
    }
  }
  return counter;
};
