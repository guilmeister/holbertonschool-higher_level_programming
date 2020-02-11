#!/usr/bin/node

const importedList = require('./100-data').list;

console.log(importedList);
const mappedArray = importedList.map(x => (x - 1) * x);
console.log(mappedArray);
