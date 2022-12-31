# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:33:20 2022

@author: HuSong
"""

import pandas as pd

'''date_range = pd.date_range(start='2022-01-01',
                           end='2022-12-31',
                           freq='W-MON')
'''

date_range = pd.date_range(start='2022-01-01',
                           periods=52,
                           freq='W-MON')

print(date_range)