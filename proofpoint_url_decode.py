# Decode ProofPoint URL Defense encoded links
# Nicholas Jelinek
# November 11th, 2019
import requests
import sys
import urllib3
import json

# Disables the SSL warnings 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    headers = {
        "Content-Type": "application/json"
    }

    url = input("Enter the encoded URL: ")
    data = {"urls": [url]}

    r = requests.post("https://tap-api-v2.proofpoint.com/v2/url/decode", headers=headers, json=data, verify=False)
   
    json_data = json.loads(r.text)
    
    for item in json_data["urls"]:
        for k,v in item.items():
            if k == "decodedUrl":
                print(f"\n{v}\n")
            else:
                continue

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboard Interruption")

while True:
    restart = input("\nWould you like to restart? (Y or N): ")
    if (restart == 'Y') or (restart == 'y'):
        main()
    else:
        sys.exit()