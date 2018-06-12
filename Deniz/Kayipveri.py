# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:07:38 2018

@author: Deniz Timartas
"""


import pandas as pd
import os

df = pd.read_pickle(os.path.join('..', 'Projects','proj', 'transactions.pickle'))

df.apply(lambda x: sum(x.isnull()))
df.apply(lambda x: len(x.unique()))


