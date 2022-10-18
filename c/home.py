import os,time

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

OS_VERSION = "19.0.0"
OS_BUILD = "1.2"

os.system('clear')
while True:
  time.sleep(2)
  print(OKGREEN+"Home"+ENDC)
  print(f"""
  {OKBLUE}[0]{ENDC} Check for Updates
  {OKBLUE}[1]{ENDC} Turn off OS
  {OKBLUE}[2]{ENDC} Kill all Tasks
  {OKBLUE}[3]{ENDC} Settings
  {OKBLUE}[4]{ENDC} Apps
  {OKBLUE}[5]{ENDC} BIOS
  {OKBLUE}[6]{ENDC} Reboot
  """)

  i = input(f"{WARNING}[?]{ENDC}{OKBLUE}")

  if i == 0:
    print("Checking for updates...")
    updater_version = open('./os/leafos-u/latest', 'r').read(1)
    if updater_version != OS_VERSION:
      print(f"An update is {OKGREEN}available{ENDC}. Would you like to update {WARNING}now?{ENDC}")
      if input(f'{WARNING}[?]{ENDC}{OKBLUE}') == "y":
        with open("./os/leafos-u/") as f: open("./os/leafos-u/")

    if updater_version == OS_VERSION:
      print(f"No updates were {FAIL}available{ENDC}.")
      os.system('clear')
