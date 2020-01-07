#!/bin/bash
# Send a request to a URL and display size of the response body
curl -sw "%{size_download}" $1 -o /dev/null ; echo

