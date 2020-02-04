#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let y = 0;
  for (; y < x; y++) {
    theFunction();
  }
};
