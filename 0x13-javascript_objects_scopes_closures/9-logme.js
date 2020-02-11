#!/usr/bin/node

let counter = 0;

exports.logMe = function (item) {
  const logList = [];
  let x = logList.length;
  logList.push(item);
  for (; x < logList.length; x++) {
    if (logList[x] === item) {
      console.log(counter + ': ' + logList[x]);
    }
  }
  counter++;
};
