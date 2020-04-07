#!/bin/bash
# Write a Bash script that takes in a URL
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1"
