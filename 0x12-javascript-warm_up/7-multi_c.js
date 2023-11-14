#!/usr/bin/node

// Check if the command line argument is undefined or not a number.
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  // Convert the command line argument to a number.
  const x = Number(process.argv[2]);

  // Initialize a counter variable.
  let i = 0;

  // Loop 'x' times and print 'C is fun'.
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
