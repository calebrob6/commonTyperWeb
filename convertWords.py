#!/usr/bin/env python

import json

f = open("google-10000-english-usa.txt","r")
lines = f.read().split("\n")
f.close()

N = 1000
topN = lines[:N]
print len(topN)

jsonString = json.dumps(topN)

f = open("words.json","w")
f.write(jsonString)
f.close()
