#!/bin/bash
# Description of task
curl -sI -w '%{response_code}' "$1" -o /dev/null
