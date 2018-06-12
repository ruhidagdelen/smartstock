# -*- coding: utf-8 -*-
"""
Created on Sat May 19 23:56:37 2018

@author: Deniz Timartas
"""

import pandas as pd
import os

CSV_PATH = os.path.join('..','Projects','proj','transactions.csv')

df = pd.read_csv(CSV_PATH)
df.to_pickle(os.path.join('..', 'Projects','proj', 'transactions.pickle'))
df = pd.read_pickle(os.path.join('..', 'Projects','proj', 'transactions.pickle'))

df[['product_id', 'product_name']]
df.iloc[ 3:14 ,2:4]

df.describe()
df.selling_price.mean()
df.selling_price.median()
df.selling_price.max()-df.selling_price.min()
df.selling_price.quantile(.25)
df.selling_price.quantile(.5)
df.selling_price.quantile(.75)
df.selling_price.var()
df.selling_price.std()


df.selling_price.plot(kind='hist', title='Yapılan Satışlar için Histogram Grafiği', color='c', bins=20)
df.selling_price.plot(kind='kde', title='Satış Fiyatları İçin KDE Grafiği', color='c')
df.groupby(['process_type']).agg({'purchase_price':'mean','selling_price':'mean'})

df_scatter = pd.read_pickle(os.path.join('..', 'Projects','proj', 'transaction_type_id.pickle'))
pd.to_numeric(df_scatter['type'])
df_scatter.plot.scatter(x='type', y='selling_price', color='c', title='Tiplere Göre Satış Kayıtları İçin Serpme Diyagramı', alpha=0.1)

