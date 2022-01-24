import os
from sys import platform

import ipapi
import requests as r


def clear_screen():
    if platform in ["linux", "linux2", "darwin"]:
        os.system("clear")

    elif platform == "win32":
        os.system("cls")


def get_ip():

    ip = r.get("https://api.ipify.org").text

    return ip


ip = get_ip()


def get_location(ip):
    data_ip = ipapi.location(ip)

    for k, v in data_ip.items():
        print(f'{k}: {v}')


def run():
    clear_screen()
    get_location(ip)


run()
