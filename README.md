# word-frequencies-bnc
Frequency of word usage in English separated by part of speech.


## Python3 and PyTest

This project uses python3 and relies on a venv virtual environment using setuptools.  

Initial setup of venv virtual environment:
```
$ python3 -m venv env
```
Creates an 'env' directory that should be at the same level as this README file.The 'env' directory should be ignored by Git.

Initial setup of pytest:
```
$ source env/bin/activate
$ pip install --upgrade pip
$ pip install pytest
$ pip install wheel
$ pip install -e packages/*
```

To deactivate the virtual environment:
```
$ deactivate
```

To activate the virtual environment after the inital setup is complete:
```
$ source env/bin/activate
```


## Word Frequencies (based on the British National Corpus)

This repository contains word frequency data that is based on the British National Corpus. The frequency lists have been provided as a companion to the book *Word Frequencies in Written and Spoken English: based on the British National Corpus* by Geoffrey Leech, Paul Rayson, Andrew Wilson (2001) pp. 320, Longman, London. ISBN 0582-32007-0

The frequency lists are licensed under Creative Commons Attribution-Share Alike 2.0 UK: England & Wales License. The license is available at https://creativecommons.org/licenses/by-sa/2.0/uk/.

The frequency lists are included exactly as provided from the website:
https://ucrel.lancs.ac.uk/bncfreq/ .

All word frequencies are given in units of per million words.
