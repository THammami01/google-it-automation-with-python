#!/bin/bash

> oldFiles.txt
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)

for file in $files; do
        temp=/home/$USER/$file

        if test -e $temp; then
                echo $temp >> oldFiles.txt
        fi
done
