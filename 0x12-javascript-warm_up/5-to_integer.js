#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('Not a number');
} else if (isNaN(Number(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[2]));
}
