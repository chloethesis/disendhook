#!/bin/bash

clear
sudo apt-get update
sudo apt-get install python3
pip install -r requirements.txt
clear
python3 disendhook.py
