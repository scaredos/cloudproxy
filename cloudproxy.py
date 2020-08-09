# Copyright (2020) @scaredos
import requests
import json
import random
import sys

zoneid = ''
key = ''


class cloudproxy():
    def __init__(self, zoneid, key):
        self.zoneid = zoneid
        self.key = key

    def createDomain(self):
        website = input('Enter the domain (example.com)> ')
        ip = input('Enter the IP to point to (127.0.0.1)> ')
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
        randomStrings = ''
        for i in range(5):
            randomStrings += random.choice(chars)
        headers = {'Authorization': f'Bearer {self.key}',
                   'Content-Type': 'application/json'}
        data = {"type": "A", "name": f"{randomStrings}.{website}",
                "content": ip, "ttl": 1, "proxied": 'true'}
        res = requests.post(
            f'https://api.cloudflare.com/client/v4/zones/{self.zoneid}/dns_records', headers=headers, json=data)
        res = json.loads(res.text)
        if res['result']['id']:
            print(f'[+] Domain     : {randomStrings}.{website}')
            print(f'[+] Identifier : {res["result"]["id"]}')
        else:
            print('[!] Failed to create new subdomain, here is the error')
            print(res)

    def removeDomain(self):
        base_url = 'https://api.cloudflare.com/client/v4/'
        ident = input('Enter the record identifier> ')
        headers = {'Authorization': f'Bearer {self.key}',
                   'Content-Type': 'application/json'}
        res = requests.delete(
            f'https://api.cloudflare.com/client/v4/zones/{self.zoneid}/dns_records/{ident}', headers=headers)
        res = json.loads(res.text)
        if res['success'] == True:
            print('[+] Deleted record!')
        else:
            print(res)


cp = cloudproxy(zoneid, key)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <option>')
        print('\t-a, --add | Add a DNS record')
        print('\t-r, --rem | Remove a DNS record')
        exit()
    print('[*] CloudProxy v1.0 | ')
    choice = sys.argv[1]
    if choice == '-a' or choice == '--add':
        cp.createDomain()
    elif choice == '-r' or choice == '--rem':
        cp.removeDomain()
    else:
        exit()
