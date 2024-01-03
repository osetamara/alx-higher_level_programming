#!/usr/bin/node
const request = require('request');

// The first argument is the API URL
const baseURL = process.argv[2];

// Make a request to the specified API URL
request(baseURL, (error, response, body) => {
  // Object to aggregate completed tasks per user
  const aggregate = {};

  // Check for errors in the request
  if (error) {
    console.log(error);
  }

  // Parse the response body as JSON
  const json = JSON.parse(body);

  // Iterate through each element in the JSON response
  json.forEach(element => {
    // Check if the task is completed
    if (element.completed) {
      // If the user is not in the aggregate object, initialize their count to 0
      if (!aggregate[element.userId]) {
        aggregate[element.userId] = 0;
      }

      // Increment the completed task count for the user
      aggregate[element.userId]++;
    }
  });

  // Output the final aggregated result
  console.log(aggregate);
});
