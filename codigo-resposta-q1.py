# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 01:30:10 2020

@author: Adriano Brito dos Santos
"""

import pandas as pd
import re


#1  INVERTE [SP][1-3] EM [1-3][SP]
def _f1(df):
    x = re.findall("[SP][1-3]",df.iloc[i,1])
    y=("".join(x))[1::-1]        
    if(x):
        df.iloc[i,1] = re.sub("[SP][1-3]",y,df.iloc[i,1],1)

#2  SIMPLIFICA NUMERO DE SINAIS +
def _f2(df):
    df.iloc[i,1] = re.sub('\++','+', df.iloc[i,1])

#3  SIMPLIFICA MULTIPLOS ESPAÇOS  
def _f3(df):
    df.iloc[i,1] = re.sub("\s+"," ",df.iloc[i,1])

#4  REMOVE HIFENS ENTRE NUMEROS  
def _f4(df):
     l = re.findall("\d-+\d",df.iloc[i,1])
     if (l):                                      
         df.iloc[i,1]=re.sub("\-+","",df.iloc[i,1])
         
#5  REMOVE ESPAÇOS ANTES DE QUALIFICADORES DE LOCAL
def _f5(df):
    x = re.findall("_ESTADO|_PAÍS|_CIDADE", df.iloc[i,1])
    y=("".join(x))                                                                
    df.iloc[i,1] = re.sub(" _ESTADO| _PAÍS| _CIDADE",y,df.iloc[i,1],1)

#6  REMOVE ESPAÇOS ANTES DE QUALIFICADORES DIRECIONAIS NA DIREITA
def _f6(df):
    z = re.findall("\s_[1-3][SP]",df.iloc[i,1])
    if (z):                                             
        df.iloc[i,1]=re.sub("\s_","_",df.iloc[i,1]) 

#7  ADICIONA ESPAÇOS APÓS OS QUALIFICADORES DIRECIONAIS PELA ESQUERDA
def _f7(df):
    s = re.findall("[1-3][SP]_", df.iloc[i,1])
    x = re.split("[1-3][SP]_", df.iloc[i,1])
    s = "".join(s)
    df.iloc[i,1] = (s+" ").join(x)
    
#8  REMOVE ESPAÇOS A ESQUERDA DE QUALIFICADORES DE INTENSIDADE
def _f8(df):
    df.iloc[i,1] = re.sub(" \(\+","(+", df.iloc[i,1])
    df.iloc[i,1] = re.sub(" \(\-","(-", df.iloc[i,1])
    
#9  SUBSTITUI ESPAÇO POR _ EM PALAVRAS PRECEDIDAS POR NÃO
def _f9(df):
    df.iloc[i,1] = re.sub("NÃO ","NÃO_", df.iloc[i,1])
    
#10 SUBSTITUI _FAMOSO(A) POR &FAMOSO(A)
def _f10(df):
    df.iloc[i,1] = re.sub("_FAMOS","&FAMOS", df.iloc[i,1])#10_FAMOSO POR &FAMOSA

#11 REMOVE PONTOS DE FRASES E NAO DE NUMEROS
def _f11(df):
    x = re.findall("\.\D", df.iloc[i,1])                
    if (x):                                            
        df.iloc[i,1] = re.sub("\.","", df.iloc[i,1])    

#12 ACRESCENTA 0 IMPLICITO
def _f12(df):
    y = re.findall("\.[0-9]", df.iloc[i,1])             
    if (y):                                             
        df.iloc[i,1] = re.sub("^\.|^ \."," 0.", df.iloc[i,1])

###############################################################################
#   #MAIN#   ##################################################################
###############################################################################

df = pd.read_csv('corpus-q1-v2.csv')

for i in range(len(df)):
    _f1(df)
    _f2(df)
    _f3(df)
    _f4(df)
    _f5(df)
    _f6(df)
    _f7(df)
    _f8(df)
    _f9(df)
    _f10(df)
    _f11(df)
    _f12(df)


#df.to_csv("corpus-resposta-q1-v2.csv",index=False)
