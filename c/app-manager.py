import os,shutil,re,time

A0 = open_filemanager
A1 = open_musicapp
A2 = open_timerapp
A3 = open_calcapp
A4 = open_coinflip

# importable from home.py and bios.py
APPS = [
  A0, A1, A2, A3, A4
]

def open_filemanager():
  print()
