#!/usr/bin/node
function findSecondMax (array) {
  const arr = array.splice(2).sort((a, b) => a - b);
  const max = Math.max.apply(null, arr);
  arr.splice(arr.indexOf(max), 1);
  return Math.max.apply(null, arr);
}
if (process.argv[2] === undefined || process.argv.length <= 3) {
  console.log('0');
  process.exit();
}
const arrays = [];
let x = 0;
for (; x < process.argv.length; x++) {
  arrays.push(process.argv[x]);
}
console.log(findSecondMax(arrays));
