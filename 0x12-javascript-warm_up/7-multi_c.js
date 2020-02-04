#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else if (isNaN(Number(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  let x = 0;
  for (; x < parseInt(process.argv[2]); x++) {
    console.log('C is fun');
  }
}
