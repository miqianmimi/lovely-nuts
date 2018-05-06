#!/bin/bash

for ((i=1; i<=10; i++)); do
	echo "Case $i:"
	cp lineupg$i.in lineupg.in
	g++ lineupg.cpp -o lineupg
	time ./lineupg
	diff --strip-trailing-cr lineupg.out lineupg$i.out
	if [ $? -eq 0 ]; then
		echo right!
	fi
	read -p 'Press Enter Key...'
done
