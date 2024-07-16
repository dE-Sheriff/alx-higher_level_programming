#!/bin/bash
# Description of task
curl -sI "$1" | grep "Allow: " | cut -d' ' -f 2-
