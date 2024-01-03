#!/usr/bin/node
const process = require('process');
const fs = require('fs');

// The first argument is the file path
const file = process.argv[2];
// The second argument is the string to write
const text = process.argv[3];

// Write the specified text to specified file in utf-8 encoding
fs.writeFile(file, text, 'utf8', function (err, data) {
  // Check if an error occurred during the writing process
  if (err) {
    // If an error occurred, print error object to console
    console.log(err);
  }
  // No error occurred, and data been written successfully
  // Additional actions or logging can added here if needed
});

