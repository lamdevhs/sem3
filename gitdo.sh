#!/bin/bash

git add $1; git status; sleep 5

git commit -m $2; git status; sleep 5

git push origin master
