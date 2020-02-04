#!/bin/bash
# Display all HTTP methods server will accept for user's URL
curl -sI "$1" | grep Allow | cut -d' ' -f2-
