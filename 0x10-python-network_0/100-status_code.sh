#!/bin/bash
# sends a request to a URL passed as an argument, displays only status code of the response.
curl -o /dev/null -sw "%{http_code}" $1
