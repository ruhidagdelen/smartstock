from django.shortcuts import render
from models import Satis
import pandas as pd


sellings = []

obj = Satis.objects.all()

for ele in obj:
	sellings.append({"product_number": ele.urunno,"product_name": ele.urunad,"date": ele.tarih,"count": ele.miktar,"price": ele.fiyat,"type": ele.uruncinsi })

df = pd.DataFrame(sellings, columns=["product_number","product_name","date","count","price","type"])
df = df.fillna(value="blank")
df.to_csv('satis.csv')
