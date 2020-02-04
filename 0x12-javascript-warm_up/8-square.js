#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  const string = 'X';
  let x = 0;
  for (; x < parseInt(process.argv[2]); x++) {
    console.log(string.repeat(process.argv[2]));
  }
}
