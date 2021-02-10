#!/usr/bin/python

import urllib3

u = "https://api.bittrex.com/api/v1.1/public/getticker?market="

t = ['btc-xmr', 'btc-eth']

h = urllib3.PoolManager()

for i in t:
    f = u + i
    r = h.request('GET', f)
    p = r.data

    print(i, p)

