# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:57:00 2021

@author: SANA
"""

import csv
import json
dict={}

of=open("airlines.csv","r")
rf=csv.reader(of)
data=list(rf)
del data[0]
       
for record in data:
    print(record)
    if record[1]  not in dict:
        dict[record[1]]=1
    else:
        dict[record[1]]+=1
print() 
       
print("Unique airport names and number of time it is repeated are:")
l=json.dumps(dict)
print(l)
print()

print("airport with Highest number of time:")
key_of_max_value=max(dict,key=dict.get)
print(key_of_max_value)
print()


print("Airport with lowest number of time:")
key_of_min_val=min(dict,key=dict.get)
print(key_of_min_val)