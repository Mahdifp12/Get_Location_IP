import ipapi
import requests as r

def get_ip():

    ip = r.get("https://api.ipify.org").text

    return ip

ip = get_ip()

def get_location(ip):
    data_ip = ipapi.location(ip)

    for k, v in data_ip.items():
        print(f'{k}: {v}')

get_location(ip)
