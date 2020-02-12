#!/usr/bin/node

const requests = require('request');
const url = process.argv[2];

requests(url, function (error, response, body) {
  if (error) {
    console.log(error)
  }
  const results = JSON.parse(body).results;
  let counter = 0;
  let x = 0;
  for (; x < results.length; x++) {
    if (results[x].characters.includes('https://swapi.co/api/people/18/')) {
      counter = counter + 1;
    }
  }
  console.log(counter);
});
