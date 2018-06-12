# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 23:40:57 2018

@author: Deniz Timartas
"""

#Sklearn kütüphanesinden svm modülünü yüklüyoruz
#Numpy kütüphanesini np adlı bir değişkenle kullanmak için hazırlıyoruz
#Matplotlib kütüphanesinin pyplot modülünü plt adlı bir değişkenle kullanmak için hazırlıyoruz
#Matplotlib kütüphanesinden style modülünü yüklüyoruz
#Ve style kütüphanesinden hazır grafik stili olan 'ggplot' ı default grafik stili olarak atıyoruz
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm

#Bu örnekte üzerinde işlem yaptığımız bir X tahmin edici ve Y hedef dizimizin olduğu var sayılmıştır.
X = np.array([[5,3],  
     [10,15],
     [15,12],
     [24,10],
     [30,45],
     [85,70],
     [71,80],
     [60,78],
     [55,52],
     [80,91],])
Y = [0,1,0,1,0,1,0,1,0,1]

#SVM tekniklerini uygulamak için basit bir svm modeli model adlı bir değişkene atanıyor. Bu modelin özellikleri adına değiştirilebilecek bir çok şey bulunmaktadır. Gruplanmanın kesin çizgilerini, grup renklerini yada daha keskin sonuçlar için daha çok işlem gücü gerektiren gamma değerini değiştirebiliriz.
model = svm.SVC(kernel='linear', C=1, gamma=1) 

#Burada modelimize elimizdeki X ve Y dizinlerini işleterek öğrenmesi sağlanıyor
model.fit(X, Y)
model.score(X, Y)

#Tahmin sonuçları burada predicted adlı bir değişkene atanıyor. Bir IDE kullanildiği yada predicted dizisi çağırıldığı takdirde atanmış tahmin değerleri kontrol edilebilir
predicted= model.predict(X)

#Aşağıda yazılmış kod satırları modelimizi bir grafik üzerinde görüntülemeye yarar.
w = model.coef_[0]
print(w)

a = -w[0] / w[1]

xx = np.linspace(0,12)
yy = a * xx - model.intercept_[0] / w[1]

h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(X[:, 0], X[:, 1], c = Y)
plt.legend()
plt.show()
