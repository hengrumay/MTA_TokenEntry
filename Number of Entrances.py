# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 17:25:17 2016

@author: choiboy9106
"""

import os
import pandas as pd
import numpy as np

os.chdir('/home/choiboy9106/Desktop/Metis/Week 1 Project Benson')
os.getcwd()

entrance = pd.read_csv("NYC_Transit_Subway_Entrance_And_Exit_Data_Original.csv")

entrance["Full Name"] = entrance["Station Name"] + " " + entrance["Subway Lines"]

count = pd.pivot_table(entrance,index=["Full Name"],aggfunc=np.size)
del count["ADA"]
del count["ADA Notes"]
del count["Corner"]
del count["Division"]
del count["East West Street"]
del count["Entrance Latitude"]
del count["Entrance Longitude"]
del count["Entrance Type"]
del count["Exit Only"]
del count["Free Crossover"]
del count["Line"]
del count["North South Street"]
del count["Staff Hours"]
del count["Staffing"]
del count["Station Latitude"]
del count["Station Location"]
del count["Station Longitude"]
del count["Station Name"]
del count["Subway Lines"]
del count["Entrance Location"]
del count["Vending"]
print(count)
count.to_csv("count.csv")