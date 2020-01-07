#!/bin/bash
# Send a POST request to User's URL w/2 vars & display the body of the response
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
