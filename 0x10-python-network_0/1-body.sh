#!/bin/bash
# takes in a URL, sends a request to that URL, and displays size of the body of the response
curl -sX GET $1 -L