#!/usr/bin/node

const importedList = require('./100-data').list;

console.log(importedList);
let x = 0;
for (; x < importedList.length; x++) {
  var mappedArray = importedList.map(x => (x - 1) * x);
}
console.log(mappedArray);
