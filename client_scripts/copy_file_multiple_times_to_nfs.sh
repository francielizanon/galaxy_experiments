#!/bin/sh
folder=$1
shift
source=$1
i=0
dest=""
for path in "$@"; do 
	dest="$dest ${folder}/${path}.${i}.txt"
	i=$(( $i + 1 ))
done
for path in $dest; do
	{
	  cp /root/$source $path
	} &
done
wait
