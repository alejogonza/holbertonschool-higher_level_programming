#!/usr/bin/node
const args = process.argv.slice(2);
const l = args.length;
if (l === 0) {
  console.log('No argument');
} else if (l === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
