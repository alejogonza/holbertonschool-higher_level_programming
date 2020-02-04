#!/usr/bin/node
let txt = 'C is fun';
let args = process.argv.slice(2);
if (+args[0]) {
  let x = +args[0];
  for (let i = 0; i < x; i++) {
    console.log(txt);
  }
} else {
  console.log('Missing number of occurrences');
}
