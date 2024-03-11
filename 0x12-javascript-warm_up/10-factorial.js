#!/usr/bin/node
function factorial (n) {
  let answer = 1;
  if (n === 0) {
    return 1;
  }
  for (let i = 2; i <= n; i++) {
    answer = answer * i;
  }
  return answer;
}

const arg1 = parseInt(process.argv[2]);
console.log(factorial(arg1));
