import os,time,shutil
from appm import apps
from reload import reloadAgent
try: from bios import start
except: pass

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
on = True
while on == True:
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
  {OKBLUE}[7]{ENDC} Reset Device
  """)

  i = input(f"{WARNING}[?]{ENDC}{OKBLUE}")

  if i == "0":
    print("Checking for updates...")
    updater_version = open('./os/leafos-u/latest', 'r').read(0)
    if updater_version != OS_VERSION:
      print(f"An update is {OKGREEN}available{ENDC}. Would you like to update {WARNING}now?{ENDC}")
      if input(f'{WARNING}[?]{ENDC}{OKBLUE}') == "y":
        with open("./os/leafos-u/c/home.py", "r") as f: 
          homeMediaCode = f.read()
        
        with open("./os/functions/home.py", "w") as f:
          f.writelines(homeMediaCode)
          
        print(f"{OKGREEN}Finished update. OS will reboot in a few seconds.{ENDC}")
        time.sleep(3)
        os.system('clear')
        on = False
        reloadAgent()

    if updater_version == OS_VERSION:
      print(f"No updates were {FAIL}available{ENDC}.")
      
  elif i == "1":
    print(f"{OKGREEN}Turned off.{ENDC}")
    on = False
    
  elif i == "2":
    print(f"{OKGREEN}Killed all tasks.{ENDC}")
  
  elif i == "3":
    print(f"{FAIL}Unknown application.{ENDC}")
  
  elif i == "4":
    print("Opening File Manager...")
    apps[0]()
    
  elif i == "5":
    print(f"{FAIL}Unknown application.{ENDC}")
    
  elif i == "6":
    print(f"{OKGREEN}Rebooting..{ENDC}")
    on = False
    reloadAgent()
  
  elif i == "7":
    print(f"{OKBLUE} Are you sure you want to reset your device? This action is unreversible. {ENDC}")
    if input(f"{WARNING}[?]{ENDC}{OKBLUE}") == "y":
      print(f"{WARNING}Resetting your device...{ENDC}")
      shutil.rmtree("./os/user/Applications")
      time.sleep(2)
      shutil.rmtree("./os/user/Desktop")
      time.sleep(2)
      shutil.rmtree("./os/user/Library")
      time.sleep(2)
      shutil.rmtree("./os/user/Downloads")
      time.sleep(2)
      shutil.rmtree("./os/user/OS")
      time.sleep(2)
      os.remove("./os/user/root.data")
      time.sleep(2)
      os.remove("./os/user/username.data")
      time.sleep(2)
      os.remove("./os/user/setup.data")
      time.sleep(2)
      
      print(f"{OKBLUE}Finished resetting your device successfully.{ENDC}")
      os.system('python /os/leafos.py &')
      on = False
