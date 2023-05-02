import requests

import json 
from termcolor import colored

banner = """
 _____ _             _      _____       __       
/  ___| |           | |    |_   _|     / _|      
\ `--.| |_ ___   ___| | __   | | _ __ | |_ ___   
 `--. \ __/ _ \ / __| |/ /   | || '_ \|  _/ _ \  
/\__/ / || (_) | (__|   <   _| || | | | || (_) | 
\____/ \__\___/ \___|_|\_\  \___/_| |_|_| \___/  
                                              
"""

print(colored(banner, "green"))

# This script uses the Alpha Vantage API to get stock information
# https://www.alphavantage.co/documentation/
# You will need to get your own API key to use this script

API_KEY="SET YOUR API KEY HERE"

while True:
    symbol = input("Enter a stock symbol(type exit to quit): ")
    if symbol.lower() == "exit":
        break
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}'
    try: 
        r = requests.get(url)
    except:
        print("\n\n")
        print(colored('Error getting stock info', "red"))
    data = r.json()
    if data == {}: 
        print("\n\n")
        print(colored("Invalid stock symbol", "red"))
    else:
       print("\n\n")
       for key, value in data.items():
        print(f"{key}: {value}")