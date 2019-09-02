#!/bin/bash

#Instal·lem pip
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
rm get-pip.py
#instal·lem els requeriments
pip3 install -r requeriments.txt
#Fem el directori on desarà les dades el bot
mkdir temp
