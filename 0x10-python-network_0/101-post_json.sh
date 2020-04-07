#!/bin/bash
# Write a Bash script that sends a JSON POST
curl -sd '@my_json_0' -H "Content-Type: application/json" -X POST "$1"
