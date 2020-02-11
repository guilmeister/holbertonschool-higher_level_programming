#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  let x = list.length - 1;
  for (; x >= 0; x--) {
    reverseList.push(list[x]);
  }
  return reverseList;
};
