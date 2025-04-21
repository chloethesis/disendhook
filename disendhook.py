#!/usr/bin/python3
import requests
import getpass
import json

# カラー設定
RESET = "\033[0m"
AQUA = "\033[96m"
RED = "\033[91m"
BOLD = "\033[1m"
WHITE = "\033[97m"
LIME = "\033[92m"

username = getpass.getuser() # ホスト名を表示

API_URL = 'https://api.host.com/' # APIの例

DISCORD_WEBHOOK_URL = '' # あなたのウェブフック

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
        send_to_discord("エラーです")

    print(LIME + BOLD + f"root@{username}" + WHITE + BOLD + ":" + AQUA + BOLD + "~" + WHITE + BOLD + "$ " + WHITE + BOLD + "ウェブフックに正常に送信されました\n" + RESET)

if __name__ == '__main__':
    main()
