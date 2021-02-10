#!/usr/bin/python

import json
import urllib3

u = "https://api.bittrex.com/api/v1.1/public/getticker?market="

t = ['btc-xmr', 'btc-eth']

h = urllib3.PoolManager()

for i in t:
    f = u + i
    r = json.loads(h.request('GET', f).data)
    d = r["result"]
    b = d["Bid"]
    a = d["Ask"]
    print(i, "Bid", b, "Ask", a)
