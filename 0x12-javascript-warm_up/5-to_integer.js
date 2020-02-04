#!/usr/bin/node
let args = process.argv.slice(2);
if (+args[0]) {
  console.log('My number: ' + args[0]);
} else {
  console.log('Not a number');
}
