#!/usr/bin/env python3
import json
s='Tx_Alcool'
print(max(json.load(open('beer_list.json')),key=lambda b:b[s] or 0)['Nom'])
