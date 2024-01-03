t process = require('process');
const fs = require('fs');

// The first argument is file path
const file = process.argv[2];

// Read the content of specified file in utf-8 encoding
fs.readFile(file, 'utf8', function (err, data) {
  // Check if an error occurred during reading process
  if (err) {
    // If an error occurred, print error object to console
    console.log(err);
  } else {
    // Output content of file to standard output (console)
    process.stdout.write(data);
  }
});
