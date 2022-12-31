# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:00:53 2022

@author: HuSong
"""
import pandas as pd

s = pd.Series(
    ['001','002','003'],
    list('abc'))

s = s.map(int)

print(s)

