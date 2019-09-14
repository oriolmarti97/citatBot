#!/bin/bash

echo 'Comencem' >sortida.log
echo 'Comencem' >errors.log
while :; do
	#Mostrem la data en la qual hem començat aquella execució, tant en els errors com en la sortida
	date >>sortida.log
	date >>errors.log
	python3 bot.py >>sortida.log 2>>errors.log
done
