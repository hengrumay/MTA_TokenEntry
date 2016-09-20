# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:57:47 2016

@author: hrm

Exploring MTA Turnstile Data

%% Refs
http://web.mta.info/developers/turnstile.html
https://data.ny.gov/Transportation/NYC-Transit-Subway-Entrance-And-Exit-Data/i9wp-a4ja/data
https://spatialityblog.com/2010/07/08/mta-gis-data-update/


%% Pandas
http://pythonhow.com/accessing-dataframe-columns-rows-and-cells

"""


#==============================================================================
#

urlList = ["http://web.mta.info/developers/data/nyct/turnstile/turnstile_160604.txt",
           "http://web.mta.info/developers/data/nyct/turnstile/turnstile_160528.txt",
           "http://web.mta.info/developers/data/nyct/turnstile/turnstile_160521.txt",
           "http://web.mta.info/developers/data/nyct/turnstile/turnstile_160514.txt",
           "http://web.mta.info/developers/data/nyct/turnstile/turnstile_160507.txt",
           "http://web.mta.info/developers/data/nyct/turnstile/turnstile_160430.txt",
           "http://web.mta.info/developers/data/nyct/turnstile/turnstile_160423.txt",
           "http://web.mta.info/developers/data/nyct/turnstile/turnstile_160409.txt",
           "http://web.mta.info/developers/data/nyct/turnstile/turnstile_160402.txt"]

#len(urlList)=9

import pandas as pd
#http://pandas.pydata.org/pandas-docs/stable/merging.html

cnt=0
for u in urlList:
    Dtmp = pd.read_csv(u)
    if cnt==0:
        Dmat = Dtmp
    else:
        Dmat = pd.concat([Dmat, Dtmp])
    cnt += 1

del Dtmp
#==============================================================================



import pandas as pd

#url = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_160402.txt"
url = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_160409.txt"
D = pd.read_csv(url)
#print(D)
#D.head

#D.columns
#Out[31]:
#Index(['C/A', 'UNIT', 'SCP', 'STATION', 'LINENAME', 'DIVISION', 'DATE', 'TIME','DESC', 'ENTRIES','EXITS'], dtype='object')



#==============================================================================
# ## Create Dictionary
#==============================================================================

#D=Dmat

import dateutil.parser as DUparser
from collections import defaultdict

Ddict = defaultdict(list)
for row in D.values:
    ca = row[0]
    unit = row[1]
    scp = row[2]
    station = row[3]
    linename = row[4]
    division = row[5]
    date = row[6]
    time = row[7]
    desc = row[8]
    entries = row[9]
    exits = row[10]

    Ddict[(ca, unit, scp, station)].append([DUparser.parse(date + " " + time), (int(entries) + int(exits))])


#==============================================================================
# some time interval [0,4,8,12,16,20,(0)]+1 discrepancies over daylight savings but also sampling times.
# however, if we take day differences in the list of commuter vol/flow count data, this might not be an issue -- day+1[0] - day[0] || or Count_8/9pm - Count_4/8am? || TimeInt[5or-1] - TimeInt[1]

#https://pymotw.com/3/datetime/

#http://travel.mtanyct.info/serviceadvisory/

#==============================================================================


## Count Passenger Vol by Station-Unit_SCP

Sdict = defaultdict(list)

for key in Ddict:
# new dict with station identifier as key and all entry/exit counts as list of values
    tmpHdict = defaultdict(list)

    for tf in Ddict[key]:
        DateTime= tf[0]
        volumn = tf[1]

        tmpHdict[DateTime.date()].append(volumn)
#        break
#        print(tmpTdict)

        ## get difference between relevant highest(latest | 8/9pm) & lowest (earliest | 4/5am) index of count of the day
    tmpCdict = defaultdict(list)
    for date in tmpHdict.keys():
#        print (date)
        #count = max(tmpTdict[date]) - min(tmpTdict[date])
        if (len(tmpHdict[date])>=2):
            count = tmpHdict[date][len(tmpHdict[date])-1] - tmpHdict[date][1]
        else:
            count = [0]

        tmpCdict[date].append(count)
    Sdict[key]= tmpCdict


#Sdict


## Cluster Count Passenger Vol by Station


