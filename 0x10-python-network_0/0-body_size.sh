#!/bin/bash
# Description of task
curl -sI "$1" | grep Content-Length | awk '{print $2}'
