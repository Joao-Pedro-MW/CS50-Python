import requests
from sys import argv as line_arguments
from sys import exit
#acces the website
bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
#convert the data to a json file
bitcoin = bitcoin.json()
#access the key BPI and after USD
bitcoin = (bitcoin['bpi'])['USD']
#get the USD bitcoin value
bitcoin_value = bitcoin['rate_float']
#convert the value from the command line to a float
try:
    user_value = float(line_arguments[1])
except ValueError:
    exit("Command-line argument is not a number")
except IndexError:
    exit("Missing command-line argument")
bitcoin_value = bitcoin_value * user_value
#output the bitcoin value formatted by thousands
print(f"${bitcoin_value:,}")