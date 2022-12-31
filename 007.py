# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:07:18 2022

@author: HuSong
"""
import pandas as pd

s = pd.Series(
    ['001','002','003'],
    list('abc'))

print(s)

print('*'*100)

s.append(pd.Series({'d':'004','e':'005'}))

print(s)

