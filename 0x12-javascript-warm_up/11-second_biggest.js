#!/usr/bin/node
let args = process.argv.slice(2);
let largest = args[0];
let nextLargest;
if (args.length < 2) {
  console.log('0');
} else if (args.length === 2) {
  if (args[0] > args[1]) {
    nextLargest = args[1];
  } else {
    nextLargest = args[0];
  }
  console.log(nextLargest);
} else {
  for (let j = 1; j < args.length; j++) {
    if (args[j] > largest) {
      nextLargest = largest;
      largest = args[j];
    } else {
      if (args[j] > nextLargest) {
        nextLargest = args[j];
      }
    }
  }
  console.log(nextLargest);
}
