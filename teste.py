# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:41:39 2020

@author: adria
"""

import pandas as pd

d = {'col1': 0, 'col2': ['OBRIGADO_AGRADECIMENTO 2S_AJUDAR_1S [PONTO]','P2_PERGUNTAR_1S', 'P3_PERGUNTAR_1S', 'S2_PERGUNTAR_1S',
                         '2P_PERGUNTAR_S2','1S_PERGUNTAR_P1','2S_PERGUNTAR_1S',
                         '12---23-3---123','1----2','13123-1',
                         'asd   asd','asdas  asd','asdasd    asd',
                         '12+++23+3++123','1++2','13123+++++1',
                         'IR RECIFE _ESTADO','IR RECIFE _CIDADE','IR RECIFE _PAÍS',
                         '1S_DAR _3P','1S_DAR _3S','1S_DAR _2P',
                         '2P_DAR_3S','3S_DAR_2S','3S_DAR_2P',
                         'AMAR (+)','VENTO (-)','TABUA (+)','COISA (-)',
                         'SOFÁ NÃO GOSTAR','OQUE NÃO GOSTAR','CASAR NÃO GOSTAR',
                         'ULLYSES_OLIVEIRA_FAMOSO','ALBERT_EINSTEIN_FAMOSO','IVETE_SANGALO_FAMOSA',
                         'IR.ONTEM. BANCO','QUERO.COMIDA.FOME','.COMER .QUERO. CADE',
                         'PAGAR 0.72',' .2','.02']}
df = pd.DataFrame(data=d)

df.to_csv("teste.csv",index=False)