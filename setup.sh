#!/bin/bash

echo 'Installing Python Dependencies'
pip install -r requirements.txt

echo 'Downloading English Core Web Model (small) from spaCy '
python -m spacy download en_core_web_sm
