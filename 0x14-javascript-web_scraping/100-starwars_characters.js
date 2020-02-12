#!/usr/bin/node

const requests = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];
requests(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const results = JSON.parse(body).characters;
  let x = 0;
  for (; x < results.length; x++) {
    requests(results[x], function (error, response, body) {
      if (error) {
        console.log(error);
      }
      const name = JSON.parse(body).name;
      console.log(name);
    });
  }
});
