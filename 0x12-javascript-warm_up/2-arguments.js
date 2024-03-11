#!/usr/bin/node
const numberOfArguments = process.argv.length - 2;
if (numberOfArguments === 0) {
  console.log('No Argument');
} else if (numberOfArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
