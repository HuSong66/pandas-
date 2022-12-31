# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:26:18 2022

@author: HuSong
"""

import pandas as pd

df = pd.DataFrame(
    {'name':['lee','wang','zhao'],
    'sex':['male','female','male'],
    'age':[10,18,24]}
    )

df.set_index('name', inplace = True)

print(df)