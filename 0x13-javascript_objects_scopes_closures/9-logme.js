#!/usr/bin/node
let res = 0;
exports.logMe = function (item) {
  console.log(res + ': ' + item);
  res += 1;
};
