# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:23:37 2020

@author: adria
"""

    
def _f7(df):
    s = re.findall("[1-3][SP]_", df.iloc[i,1])
    x = re.split("[1-3][SP]_", df.iloc[i,1])
    s = "".join(s)
    df.iloc[i,1] = (s+" ").join(x)
    

import pandas as pd
import re

df = pd.read_csv('teste.csv')

for i in range(len(df)):
    _f7(df)
    
    

    
    

        