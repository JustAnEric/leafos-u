import os,shutil,re,time

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

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
