#!/usr/bin/env python3
import json
j=open('beer_list.json')
B=json.load(j)
s='Tx_Alcool'
print(max((b for b in B if b[s]),key=lambda b:b[s])['Nom'])
