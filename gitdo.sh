#!/bin/bash

# usage:
# ./gitdo.sh <what to add> <commit name>

# trick:
# echo foo{,} --> foo foo

function br() {
  echo "----------------"
}

git config --global user.email lam.dev.hs@gmail.com
git config --global user.name lamdevhs

br; br
git status; git add $1; br; git status; br;
echo -n "next step: commit -m $2 ; status " ; read

git commit -m $2; br; git status; br;
echo -n "next step: push " ; read

br; git push origin master
