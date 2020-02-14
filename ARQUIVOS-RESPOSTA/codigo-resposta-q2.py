# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 01:00:31 2020

@author: Adriano Brito dos Santos
"""

import pandas as pd
import json
from unicodedata import normalize


df = pd.read_csv('corpus-q2.csv')

def word_count(string):
    counts = {}
    for l in string:
        l = normalize('NFKD', l).encode('ASCII','ignore').decode('ASCII')
        words = l.split(" ")
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
            with open('ocorrencias.json', 'w') as f:
                json.dump(counts, f)
        

word_count(df['gr'])
