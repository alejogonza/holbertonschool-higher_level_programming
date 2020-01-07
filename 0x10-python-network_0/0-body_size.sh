#!/bin/bash
# Send a request to a URL and display size of the response body
curl -so /dev/null -w '%{size_download}\n' "$1"

