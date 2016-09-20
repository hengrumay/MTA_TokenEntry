# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 17:01:34 2016

@author: choiboy9106
"""

import pandas as pd
import matplotlib.pyplot as plt

#import and store MTA turnstile data from April and May into weekly variables
week1 = pd.read_csv("http://web.mta.info/developers/data/nyct/turnstile/turnstile_160409.txt")
week2 = pd.read_csv("http://web.mta.info/developers/data/nyct/turnstile/turnstile_160416.txt")
week3 = pd.read_csv("http://web.mta.info/developers/data/nyct/turnstile/turnstile_160423.txt")
week4 = pd.read_csv("http://web.mta.info/developers/data/nyct/turnstile/turnstile_160430.txt")
week5 = pd.read_csv("http://web.mta.info/developers/data/nyct/turnstile/turnstile_160507.txt")
week6 = pd.read_csv("http://web.mta.info/developers/data/nyct/turnstile/turnstile_160514.txt")
week7 = pd.read_csv("http://web.mta.info/developers/data/nyct/turnstile/turnstile_160521.txt")
week8 = pd.read_csv("http://web.mta.info/developers/data/nyct/turnstile/turnstile_160528.txt")
week9 = pd.read_csv("http://web.mta.info/developers/data/nyct/turnstile/turnstile_160604.txt")
year2016 = pd.concat([week1,week2,week3,week4,week5,week6,week7,week8,week9])
year2016 = year2016.rename(columns=lambda x:x.strip()) #used to strip whitespace

year2016["Shifted Entries"] = pd.Series(year2016["ENTRIES"]).shift(-1) #shift by 1 row up
year2016["Shifted Exits"] = pd.Series(year2016["EXITS"]).shift(-1) #shift by 1 row up

year2016["Entries Diff"] = year2016["Shifted Entries"] - year2016["ENTRIES"]
year2016["Exits Diff"] = year2016["Shifted Exits"] - year2016["EXITS"]

print(year2016)

#print(pd.to_datetime(year20161["DATE"]+ " " + year20161["TIME"]))

#print(year20161.describe())
#print(pd.pivot_table(year20161,index=["SCP"]))s