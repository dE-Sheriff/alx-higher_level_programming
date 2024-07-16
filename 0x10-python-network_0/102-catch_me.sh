#!/bin/bash
# Description of task
curl -sX PUT -L -d "user_id=98" --header "origin: School" 0.0.0.0:5000/catch_me
