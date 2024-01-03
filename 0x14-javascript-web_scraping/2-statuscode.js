t process = require('process');
const request = require('request');

// The first argument is the URL to request (GET)
const url = process.argv[2];

// Make a GET request to the specified URL
request(url, function (error, response) {
  // Check if there is no error during the request
  if (error == null) {
    // Display the status code of the GET request
    console.log(`code: ${response.statusCode}`);
  }
  // If there is error,won't logged here; you may add error handling
});
