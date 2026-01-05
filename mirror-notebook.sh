#!/bin/bash

FILE_ID="1Aub2_Zd2wSa0g1ZrCQWGzQJuAp-bZLpv"
curl -L \
  "https://drive.usercontent.google.com/download?id=${FILE_ID}&export=download&confirm" \
  -o notebook.ipynb
