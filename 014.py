# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:51:46 2022

@author: HuSong
"""

import pandas as pd

date_range = pd.date_range(start='2022-01-01',
                           periods=52,
                           freq='W-MON')

df = pd.DataFrame(data=date_range,
                  columns=['day'],
                  )

df['day_of_year'] = df['day'].dt.dayofyear

print(df)