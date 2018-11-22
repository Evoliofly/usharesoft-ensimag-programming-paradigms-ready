#!/usr/bin/env python3
import json
j=open('beer_list.json')
B=json.load(j)
print(max((b for b in B if b['Tx_Alcool']),key=lambda b:b['Tx_Alcool'])['Nom'])
