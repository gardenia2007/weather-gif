#!/bin/bash

for i in `ls $1` ;
do
	d=$d" "$i"/*"
done

cd $1
animate -delay 10 $d


