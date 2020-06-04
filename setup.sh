#!/bin/bash

#Instal·lem pip
#wget https://bootstrap.pypa.io/get-pip.py
#python3 get-pip.py
#rm get-pip.py
#instal·lem els requeriments
pip3 install -r requeriments.txt
#Instal·lem cutycapt, per fer les captures, i xvfp, per poder correr un programa que requereix tenir X11 sense tenir-lo
apt update
apt install cutycapt
apt install xvfb
#Fem el directori on desarà les dades el bot
mkdir temp
