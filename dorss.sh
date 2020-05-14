#!/bin/bash

date
cd /path/to/site
cp skeltop.html tmp.html
./dorss.py >> tmp.html
cat skelbot.html >> tmp.html
mv tmp.html index.html
date
