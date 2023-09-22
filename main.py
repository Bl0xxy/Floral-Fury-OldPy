if __name__ != '__main__': exit()

### IMPORTS ###
print("Importing Modules...")
import sys
from termcolor import colored
import time
import json
import os

time.sleep(0.2)

### FILE LOADING ###
print(colored("Loading Data...", 'cyan'))
with open('lang.json', 'r', encoding='utf-8') as f:
  lang = json.load(f)
with open('save.json', 'r+', encoding='utf-8') as f:
  save = json.load(f)
time.sleep(0.2)


### FUNCTIONS ###
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')


def custom_print(msg: str, delay: float = 0.03, newline=True):
  for c in msg:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(delay)
  if newline:
    print()



clear()
custom_print(colored(lang['welcome'], 'green'))
time.sleep(2)
clear()
custom_print(colored(lang['usr_create'], 'light_blue'), newline=False)
username = input()
clear()
custom_print(colored(lang['start'], 'light_blue'), delay=0.00)
input("Press ENTER to Continue...")


