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

global open_filemanager
global open_musicapp
global open_timerapp
global open_calcapp
global open_coinflip

def open_filemanager():
  Open = True
  while Open:
    os.system("clear")
    filel = []
    path = "./os/"
    for file in os.listdir(path):
      filel.append(file)
    count = 0
    for line in filel:
      print(f"{OKBLUE}[{count}]{ENDC} {line}")
      count=count+1
    i=input("[?] Jump to a directory or file... ")
    i2 = int(i)
    if filel[i2]:
      if os.path.isdir(filel[i2]):
        return path = filel[i2]
      else: 
        print("The thing you selected was a file. Open it in a file to edit and view.")
        time.sleep(5)
    else: 
      print("No such file or directory.")
      time.sleep(5)
      
def open_musicapp(): return None
def open_timerapp(): return None
def open_calcapp(): return None
def open_coinflip(): return None

A0 = open_filemanager
A1 = open_musicapp
A2 = open_timerapp
A3 = open_calcapp
A4 = open_coinflip

# importable from home.py and bios.py
apps = [
  A0, A1, A2, A3, A4
]
