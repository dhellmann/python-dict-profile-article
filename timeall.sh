#!/bin/sh

for f in t-*.py
do
    echo $f
    echo
    python dotime.py $f
    python -m dis $f
    echo
done
