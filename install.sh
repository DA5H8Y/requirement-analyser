#! /usr/bin/bash
python -m venv .env
source .env/bin/activate
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm