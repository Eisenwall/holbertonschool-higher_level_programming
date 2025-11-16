#!/usr/bin/node

const arg = process.argv[2]; // first argument
const num = parseInt(arg, 10);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
