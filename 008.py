# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:15:55 2022

@author: HuSong
"""

import pandas as pd

s = pd.Series(
    ['001','002','003'],
    list('abc'))

df = s.reset_index()

df.columns = ['alpha','numbers']

print(df)