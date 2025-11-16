#!/usr/bin/node

const x = parseInt(process.argv[2], 10);

if (isNaN(x) || x <= 0) {
  // Do nothing
} else {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
