##Made By ❟❛❟ | $eba#0001
##Don't skid and give cred

import random
from random import *
from random import randrange, choice
from string import ascii_letters, digits
from threading import Thread as thr
from pypresence import Presence
from itertools import cycle
from datetime import date
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os

print(f"""
{Fore.RED}
▀█▀ ░█▀▀▄ 　 ░█▀▀█ █──█ █── █── █▀▀ █▀▀█ 
░█─ ░█─░█ 　 ░█▄▄█ █──█ █── █── █▀▀ █▄▄▀ 
▄█▄ ░█▄▄▀ 　 ░█─── ─▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀─▀▀
{Fore.WHITE}          Installing ID Tools
""")
print(f"{Fore.RED}")
progressbar = tqdm([2,4,6,8,10])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Loading: ')

import base64, pyperclip

print(f"""
{Fore.RED}
░█▀▀▀█ █▀▀ █▀▀▄ █▀▀█ █ █▀▀ 　 ░█▀▀█ █──█ █── █── █▀▀ █▀▀█ 
─▀▀▀▄▄ █▀▀ █▀▀▄ █▄▄█ ─ ▀▀█ 　 ░█▄▄█ █──█ █── █── █▀▀ █▄▄▀ 
░█▄▄▄█ ▀▀▀ ▀▀▀─ ▀──▀ ─ ▀▀▀ 　 ░█─── ─▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀─▀▀
{Fore.WHITE}                       INSERT ID
""")

id = input(Fore.RED+" root" + Fore.WHITE+"@" + Fore.RED+"$eba.tools" + Fore.WHITE+":" + Fore.CYAN+"~" + Fore.RED+"ID" + Fore.WHITE+" ")

try:
    check = int(id)
    print('')
    print(f'{Fore.RED} [{Fore.WHITE}+{Fore.RED}] Your ID is currently valid.')
    data = f'{id}'
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print('')
    print(f'{Fore.RED} [{Fore.WHITE}+{Fore.RED}] {encodedStr}')
    print('')
    copy = input(f'{Fore.RED} [{Fore.WHITE}+{Fore.RED}] Do you want copy this text? (y/n){Fore.WHITE} ')

    if copy == "y":
        pyperclip.copy(encodedStr)
        print('')
        print(f'{Fore.RED} [{Fore.WHITE}+{Fore.RED}] Text Copied!')

    if copy == "Y":
        pyperclip.copy(encodedStr)
        print('')
        print(f'{Fore.RED} [{Fore.WHITE}+{Fore.RED}] Text Copied!')

    else:
        print('')
        print(f'{Fore.RED} [{Fore.WHITE}+{Fore.RED}] Press enter to Exit')
        input()

except ValueError:
    print('')
    print(f'{Fore.RED} [{Fore.WHITE}+{Fore.RED}] Invalid ID!')
    print('')
    print(f'{Fore.RED} [{Fore.WHITE}+{Fore.RED}] Press enter to Exit')
    input()
