#!/usr/bin/env python3
import json
s='Tx_Alcool'
print(max((b for b in json.load(open('beer_list.json')) if b[s]),key=lambda b:b[s])['Nom'])
