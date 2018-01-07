#!/bin/bash

# usage:
# ./gitdo.sh <what to add> <commit name>

# trick:
# echo foo{,} --> foo foo

git config --global user.email lam.dev.hs@gmail.com
git config --global user.name lamdevhs

git add $1; git status
echo "next step: commit -m $2 ; status" ; sleep 5

git commit -m $2; git status
echo "next step: push" ; sleep 5

git push origin master
