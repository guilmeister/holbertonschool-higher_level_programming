#!/usr/bin/node

const requests = require('request');
const url = process.argv[2];

requests.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const users = JSON.parse(body).reduce((accumulator, currentValue) => {
    if (currentValue.completed) {
      accumulator[currentValue.userId]++;
    } else {
      accumulator[currentValue.userId] = 1;
    }
    return accumulator;
  }, {});
  console.log(users);
});
