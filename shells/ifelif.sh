#!/bin/bash

a=0

echo -n "Input : "
read a 

if [ $a -ge 90 ]; then
    echo A
elif [ $a -ge 80 ]; then
    echo B
elif [ $a -ge 70 ]; then
    echo C
elif [ $a -ge 60 ]; then
    echo D
elif [ $a -ge 80 ]; then
    echo D
fi

echo "Thank you~ Bye~"

    