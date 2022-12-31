# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:42:47 2022

@author: HuSong
"""

import pandas as pd

'''date_range = pd.date_range(start='2022-01-01',
                           freq='H',
                           periods=24)
'''

date_range = pd.date_range(start='2022-01-01',
                           freq='H',
                           end='2022-01-02',
                           inclusive=('left'))

print(date_range)
