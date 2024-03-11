#!/usr/bin/node
const arg1 = process.argv[2];
const convertedNumber = parseInt(arg1);
if (!isNaN(convertedNumber)) {
  console.log(convertedNumber);
} else {
  console.log('Not a number');
}
