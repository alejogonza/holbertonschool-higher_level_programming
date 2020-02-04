#!/usr/bin/node
function factorial (a) {
  if (a <= 0) {
    return 1;
  }
  if (a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

let args = process.argv.slice(2);
if (+args[0]) {
  console.log(factorial(+args[0]));
} else {
  console.log('1');
}
