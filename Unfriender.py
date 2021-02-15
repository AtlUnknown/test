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


token = input("Enter token noob : ")

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
    print('[+] Valid token')
    input("Press any key")
else:
    print(f'[{Fore.RED}-{Fore.RESET}] Wrong token tuff')
    input("Press any key")
    exit(0)
Clear()


print(f''' 
            ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗     ██████╗ ██╗   ██╗    ██╗  ██╗███████╗██╗   ██╗ ██████╗ 
            ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝    ██║  ██║██╔════╝╚██╗ ██╔╝██╔═══██╗
            ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝    ██████╔╝ ╚████╔╝     ███████║█████╗   ╚████╔╝ ██║   ██║
            ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗    ██╔══██╗  ╚██╔╝      ██╔══██║██╔══╝    ╚██╔╝  ██║   ██║
            ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║    ██████╔╝   ██║       ██║  ██║███████╗   ██║   ╚██████╔╝
            ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═════╝    ╚═╝       ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ 
                                                                                                       ''')

client = discord.Client()

@client.event
async def on_connect():
    print('Unfriending friends')
    for user in client.user.friends:
	        try:
	            await user.remove_friend()
	            print(f'unfriended {user}')
	        except:
	            print(f"can't unfriend {user}")


client.run(token, bot=False)
