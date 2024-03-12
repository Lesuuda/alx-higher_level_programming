#!/usr/bin/node
const arg1 = process.argv[2];
const numberOfOccurrences = parseInt(arg1);
if (!isNaN(numberOfOccurrences)) {
  for (let i = 0; i < numberOfOccurrences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
