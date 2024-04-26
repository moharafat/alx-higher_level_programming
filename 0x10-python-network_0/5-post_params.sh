#!/bin/bash
# sends a POST request passed URL, and displays body response
curl -s -X POST "email=test@gmail.com&subject=I will always be here for PLD" "${1}"
