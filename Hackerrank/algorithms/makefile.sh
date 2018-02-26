#!/bin/bash

# Usage: ./makefile.sh <folder> <filename>
if [ -z $1 ] || [ -z $2 ]
then
  echo "Usage: ./makefile.sh <folder> <filename>"
  exit 1
fi

if ! [ -d $1/data ]
then
  mkdir $1/data
fi

sed s/file_name/$2/g initial_data.py > $1/$2.py && touch $1/data/$2.txt
