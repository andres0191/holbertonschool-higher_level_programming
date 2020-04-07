#!/bin/bash
# Write a Bash script that takes in a URL
curl -sX OPTIONS "$1" -I | grep "Allow" | cut -d ' ' -f2-
