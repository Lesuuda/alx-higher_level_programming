#!/usr/bin/node
let input = 0;
exports.logMe = function (item) {
  console.log(input + ':' + item);
  input++;
};
