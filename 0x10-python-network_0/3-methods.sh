#!/bin/bash
#DELETE request to the URL passed as1st argument & Display Body's response
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
