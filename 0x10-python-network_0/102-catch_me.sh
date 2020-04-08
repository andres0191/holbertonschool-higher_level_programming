#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -sLH "You got me!-User-Id:98" "0.0.0.0:5000/catch_me"
