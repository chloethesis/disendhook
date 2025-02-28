#!/bin/bash

sudo apt-get update
pip install -r requirements.txt
clear
python3 disendhook.py
