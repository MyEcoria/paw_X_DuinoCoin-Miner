from pyduinocoin import DuinoClient
import json
import requests
import re
import math
import time

# The address of your RPC node:
url = 'Replace me'

client = DuinoClient()
username = 'Replace me'  # Input username

try:
    result = client.user(username)
except Exception as error:
    print(error)
else:
    print('Balance: ' + str(result.balance.balance))

    print('Miners: ')
    for miner in result.miners:
        print(miner)
        accepted = miner["accepted"]
        adresse = miner["identifier"]
        hash = miner["hashrate"]
        hash = int(hash) / 1000
        envoie = hash * 0.0937984496124031
        print(envoie)
        envoie = math.trunc(envoie)
        adresse = re.sub(' ', '_', adresse)
        send = send = '{ "action": "send", "wallet": "Replace me", "source": "Replace me", "destination": "' + \
            adresse + '", "amount": "' + \
            str(envoie) + '000000000000000000000000000" }'
        print(send)
        send = json.loads(send)
        sending = requests.post(url, json=send)
        sending = sending.text
        print(sending)
