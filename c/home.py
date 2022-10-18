import os,time

class col:
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
print("Home")
print("""
[0] Check for Updates
[1] Turn off OS
[2] Kill all Tasks
[3] Settings
[4] Apps
[5] BIOS
[6] Reboot
""")
