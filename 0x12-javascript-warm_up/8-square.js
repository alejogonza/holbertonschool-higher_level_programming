#!/usr/bin/node
let args = process.argv.slice(2);
if (+args[0]) {
  let x = +args[0];
  let txt = Array(x + 1).join('X');
  for (let j = 0; j < x; j++) {
    console.log(txt);
  }
} else {
  console.log('Missing size');
}
