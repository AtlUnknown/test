import discord
import os
import ctypes
import colorama
import requests
import time
from colorama import Fore



def Clear():
    os.system('cls')
Clear()


while True:
    password = input("[+] Enter Password: ")
    if password =="HeyoW":
        print("Correct password")
        input("[+] enter to continue to Selfbot")
        break
    else:
        print("In Correct password")
Clear()

while True:
    Text = input("[+] Enter Text you want to send : ")
    if Text =="TEXT_HERE":
        print("you forgot to add text")
        input("Wyd you didnt add text")
        exit(0)
    else:
        print("[+] Enter to continue to nuker")
        break
Clear()


token = input("Enter token cuminabun : ")

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
    print('[+] Valid token')
    input("Press Any Key To Start Massdming")
else:
    print(f'[{Fore.RED}-{Fore.RESET}] Wrong token rip')
    input("Press Any Key To Redo")
    exit(0)
Clear()


print(f'''{Fore.MAGENTA}          
           ██████╗ ██████╗ ███╗   ███╗███████╗██╗   ██╗    ███╗   ███╗ █████╗ ███████╗███████╗██████╗ ███╗   ███╗
          ██╔═══██╗██╔══██╗████╗ ████║╚══███╔╝╚██╗ ██╔╝    ████╗ ████║██╔══██╗██╔════╝██╔════╝██╔══██╗████╗ ████║
          ██║   ██║██████╔╝██╔████╔██║  ███╔╝  ╚████╔╝     ██╔████╔██║███████║███████╗███████╗██║  ██║██╔████╔██║
          ██║   ██║██╔══██╗██║╚██╔╝██║ ███╔╝    ╚██╔╝      ██║╚██╔╝██║██╔══██║╚════██║╚════██║██║  ██║██║╚██╔╝██║
          ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗   ██║       ██║ ╚═╝ ██║██║  ██║███████║███████║██████╔╝██║ ╚═╝ ██║
           ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═════╝ ╚═╝     ╚═╝
                                                                                                       ''')

client = discord.Client()


@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      ORMZY = discord.Embed(color= discord.Color(0x9400D3))
      ORMZY.set_author(name="MASSDMER BY JLORMZY / XYMELI")
      ORMZY.add_field(name="ORMZY MASSDMER",value=Text)
      ORMZY.set_image(url="https://media.discordapp.net/attachments/802540380587425804/803343650431959090/image0_6.gif")
      await user.send(embed=ORMZYW)
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")
       print(f"Directed messaged all users friends")


client.run(token, bot=False)
