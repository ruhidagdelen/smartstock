import pandas as pd
import os

CSV_PATH = os.path.join('..','Projects','Jupyter Projects','test.csv')

df = pd.read_csv(CSV_PATH)

#COLS_TO_USE=['id','artist','title','medium','year','acquisitionYear','height','width','units']

df = pd.read_csv(CSV_PATH)

df.to_pickle(os.path.join('..', 'Projects','Jupyter Projects', 'test.pickle'))
