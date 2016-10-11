# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 04:33:00 2016

@author: hrm
"""

filepath = '/Users/hrm/Documents/Dropbox/DSrelated/Metis/MTA_turnstile/'

import os
if os.getcwd() == filepath:
    filepath = ''
else:
    os.chdir(filepath)
    filepath = ''


import pandas as pd
#import numpy as np
import pickle

#from collections import defaultdict


filename = ["turnstile_160604",
           "turnstile_160528",
           "turnstile_160521",
           "turnstile_160514",
           "turnstile_160507",
           "turnstile_160430",
           "turnstile_160423",
           "turnstile_160409",
           "turnstile_160402"]

#WKs = np.arange(1,len(filename)+1)

combineDF=pd.DataFrame()

for f in filename:
#    print(f)
    pklfile1 = f +'_1'+'.pkl'
#    print(pklfile1)
    with open(pklfile1, 'rb') as picklefile:
        data1 = pd.DataFrame(pickle.load(picklefile))

        data1.columns=['stat','counts']
        data2 = data1.sort(columns=1, ascending=False)

        data2.to_csv('pklfile1.csv')


#    data1_Dict = dict(zip(data1[0], data1[1]))
#
#    Ddict = defaultdict(list)
#    for k, v in data1_Dict.items():
#        Ddict[k].append(v)


for f in filename:
    print(f)
    pklfile0 = f+'_0'+'.pkl'
    #pklfile0 = filename[n]+'_0'+'.pkl'
    print(pklfile0)

    with open(pklfile0, 'rb') as picklefile:
        data0 = pd.DataFrame(pickle.load(picklefile))
#        data0 = pickle.load(picklefile)

#    data0_Dict = dict(zip(data1[0], data1[1]))
#
#    Ddict = defaultdict(list)
#    for k, v in data1_Dict.items():
#        Ddict[k].append(v)




#with open(pklfile1, 'rb') as picklefile:
#    data1a = pd.DataFrame(pickle.load(picklefile))

# with open('StatFlowDF0_test.pkl', 'rb') as picklefile:
#     data = pd.DataFrame(pickle.load(picklefile))

with open(pklfile0, 'rb') as picklefile:
    data0 = pd.DataFrame(pickle.load(picklefile))


data1_Dict = dict(zip(data1[0], data1[1]))
data1a_Dict = dict(zip(data1a[0], data1a[1]))


#pd.concat([data1, data1a], axis=1, keys=list(data1_Dict.keys()) )

pd.concat([data1, data1a[1]], axis=1 , ignore_index=True)

pd.concat([data1, data1a[1]], axis=1, join_axes=[data1a.index])

#data1_Dict.append(data1a_Dict, ignore_index=True)

#pd.merge(data1, data1a, on='key')


#collect via loop and build dict to append the counts... all unique names!