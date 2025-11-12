#!/bin/bash
# Simple traffic generator for the tutorial app
while true; do
  curl -s http://localhost:5000 > /dev/null
  sleep $((RANDOM % 3 + 1))
done
