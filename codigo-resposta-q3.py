# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:51:04 2020

@author: Adriano Brito dos Santos
"""

import pandas as pd
import re

df = pd.read_csv('corpus-q3.csv')

def data_augmentation(df):
    dataframe = []
    for k in range(len(df)):
        linha = re.split("[1-3][SP]",df.iloc[k,1])
        string ="".join(linha)
        qualific = ['1S','2S','3S','1P','2P','3P']
        for i in qualific:
            for j in qualific: 
                y = re.sub("\s_"," "+i+"_",string)
                data = re.sub("_\s","_"+j+" ",y)
                dataframe = [df.iloc[k,0],data]
                df.loc[len(df)] = dataframe
    df.drop_duplicates(keep='last',inplace=True)          
    

data_augmentation(df)


#df.to_csv("corpus-resposta-q3.csv",index=False)

                    
            