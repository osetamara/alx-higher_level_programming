#!/usr/bin/node

// Check if the command line argument is not a number or is undefined.
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not a number');
} else {
  // If the command line argument is a number, parse it and print the result.
  console.log('My number:', parseInt(process.argv[2]));
}
