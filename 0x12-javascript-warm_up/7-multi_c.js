#!/usr/bin/node
const txt = 'C is fun';
const args = process.argv.slice(2);
if (+args[0]) {
  const x = +args[0];
  for (let i = 0; i < x; i++) {
    console.log(txt);
  }
} else {
  console.log('Missing number of occurrences');
}
