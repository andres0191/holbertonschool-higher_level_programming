#!/bin/bash
# Write a Bash script that sends a request
curl -s -o /dev/null -w "%{http_code}" "$1"
