#!/usr/bin/node
const args = process.argv.slice(2);
if (+args[0]) {
  const x = +args[0];
  const txt = Array(x + 1).join('X');
  for (const j = 0; j < x; j++) {
    console.log(txt);
  }
} else {
  console.log('Missing size');
}
