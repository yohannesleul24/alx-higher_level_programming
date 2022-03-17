#!/bin/bash
# Bash Script that takes in a URL as an argument, sends a GET request to the URL
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
