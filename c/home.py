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

os.system('clear')
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
