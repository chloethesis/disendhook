#!/usr/bin/python3
import requests
import getpass
import json

# COLOUR SETTING
RESET = "\033[0m"
AQUA = "\033[96m"
RED = "\033[91m"
BOLD = "\033[1m"
WHITE = "\033[97m"
LIME = "\033[92m"

# DO NOT REMOVE
username = getpass.getuser() # DISPLAY USERNAME

API_URL = '' # YOUR API URL 

DISCORD_WEBHOOK_URL = '' # YOUR WEBHOOK

def get_api_data(query):
    try:
        response = requests.get(API_URL + query)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException:
        return None

def send_to_discord(data):
    message = {
        'content': data
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=message)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        pass

def main():
    print(RED + BOLD + "\n██████╗ ██╗███████╗███████╗███╗   ██╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗" + RESET)
    print(RED + BOLD + "██╔══██╗██║██╔════╝██╔════╝████╗  ██║██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝" + RESET)
    print(RED + BOLD + "██║  ██║██║███████╗█████╗  ██╔██╗ ██║██║  ██║███████║██║   ██║██║   ██║█████╔╝" + RESET) 
    print(RED + BOLD + "██║  ██║██║╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══██║██║   ██║██║   ██║██╔═██╗" + RESET)
    print(RED + BOLD + "██████╔╝██║███████║███████╗██║ ╚████║██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗" + RESET)
    print(RED + BOLD + "╚═════╝ ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝\n" + RESET)

    query = input(LIME + BOLD + f"root@{username}" + WHITE + BOLD + ":" + AQUA + BOLD + "~" + WHITE + BOLD + "$ " + RESET)

    api_data = get_api_data(query)
    
    if api_data:
        send_to_discord(api_data)
    else:
        send_to_discord("GUEST ERROR")

    print(LIME + BOLD + f"root@{username}" + WHITE + BOLD + ":" + AQUA + BOLD + "~" + WHITE + BOLD + "$ " + WHITE + BOLD + "SUCCESSFULLY SEND VIA WEBHOOK!\n" + RESET)

if __name__ == '__main__':
    main()
