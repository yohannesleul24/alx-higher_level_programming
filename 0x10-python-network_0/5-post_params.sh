#!/bin/bash
# Bash Script that takes in a URL as an argument, sends a GET request to the URL
curl -sX POST -d "email=hr@yohannesleul24.com&subject=I will always be here for PLD" "$1"
