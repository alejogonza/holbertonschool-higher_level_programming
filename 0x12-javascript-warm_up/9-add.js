#!/usr/bin/node
function add (a, b) {
  if (+a && +b) {
    return a + b;
  } else {
    return NaN;
  }
}

let args = process.argv.slice(2);
console.log(add(+args[0], +args[1]));
