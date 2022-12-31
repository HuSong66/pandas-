# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:29:54 2022

@author: HuSong
"""

import pandas as pd

date_range = pd.date_range(start='2022-12-01',
                           end='2022-12-31')

date_range1= pd.date_range(start='2022-12-01',
                           periods=31)

print(date_range)

print('*'*100)

print(date_range1)