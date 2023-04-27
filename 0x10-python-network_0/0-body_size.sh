#!/bin/bash
# sends a request to the url that displays the size of the response body in bytes
curl -s "$1" | wc -c
