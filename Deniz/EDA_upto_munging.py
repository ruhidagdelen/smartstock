# -*- coding: utf-8 -*-
"""
Created on Sat May 12 17:48:43 2018

@author: Deniz Timartas
"""
import pandas as pd
import os

df_train = pd.read_pickle(os.path.join('..', 'Projects','Jupyter Projects', 'train.pickle'))
df_test = pd.read_pickle(os.path.join('..', 'Projects','Jupyter Projects', 'test.pickle'))

df[['Name', 'Age']]
df_train.info()
df_test['Survived']=-888
df=pd.concat((df_train, df_test),axis=0)
#EDA:SUMMARY
df.Fare.mean()
df.Fare.median()
df.Fare.max()-df.Fare.min()
df.Fare.quantile(.25)
df.Fare.quantile(.5)
df.Fare.quantile(.75)
df.Fare.var()
df.Fare.std()
matplotlib inline
df.Fare.plot(kind='box')
df.Age.plot(kind='hist', title='histogram for Age', color='c', bins=20)
df.Age.plot(kind='kde', title='kde for Age', color='c')
df.plot.scatter(x='Age', y='Fare', color='c', title='Scatter Plot: Age Class vs Fare', alpha=0.15)

df.describe(include='all')
df.Pclass.value_counts().plot(kind='bar',rot=0,color='c')

#EDA:DISTRIBUTIONS we got kinds of histogram, kde, bar, rot
df.Age.plot(kind='hist',title='Age Graph',color='c', bins=20)

#bivariate graph - Scatter for Class vs. Fare. alpha for density analysis
df.plot.scatter(x='Pclass', y='Fare', color='c', title='Scatter Graph', alpha=0.35)

#Grouping
#Getting statistics
df.groupby('Sex').Age.median()
df.groupby(['Pclass'])['Fare','Age'].median()
df.groupby(['Pclass']).agg({'Fare':'mean','Age':'median'})

#Crosstab
pd.crosstab(df.Sex,df.Pclass)
pd.crosstab(df.Sex,df.Pclass).plot(kind='bar')

#Pivot
df.pivot_table(index='Sex',columns='Pclass',values='Age',aggfunc='mean')
df.pivot_table(index='Sex',columns='Pclass',values='Age',aggfunc='mean').plot(kind='bar',title='Age Mean')
