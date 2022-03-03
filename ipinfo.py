import requests 
import pandas as pd 
import argparse
from ipaddress import ip_address

parser = argparse.ArgumentParser(description="Query ipinfo.io")
parser.add_argument('-i', '--ip', nargs=1, type=ip_address, help='Single IP address that you want to query')
args = parser.parse_args() 

def main():
    access_token = "<access token here>"

    url = f"http://ipinfo.io/{args.ip[0]}"

    response = requests.get(url, params=access_token).json()

    df = pd.DataFrame([response])

    for k,v in response.items():
        print(f"{k:<10} {v}")

if __name__ == '__main__':
    main()
