# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 03:51:04 2020

@author: TOSHIBA
"""

import  pandas as pd
data=pd.read_csv("yepyeni.csv")
data=data.drop("filename", axis=1)
data=data.drop("mfcc2", axis=1)
x=data.drop('label',axis=1)
#%% string olan label değerlerini sayısal değere dönüştürdü
from sklearn.preprocessing import LabelEncoder
genre_list = data.iloc[:, -1]
encoder = LabelEncoder()
data.label = encoder.fit_transform(genre_list)
y=data.label
#%% Veriseti test ve train olarak ayrılıyor
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2)

#%%  Training aşaması
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


rfc = RandomForestClassifier(n_estimators=90,random_state=0,max_features='sqrt')
rfc.fit(x_train,y_train)
rf=rfc.feature_importances_

# Test veri kümemi verdim ve tahmin işlemini gerçekleştirdim
result2 = rfc.predict(x_test)
accuracy1 = accuracy_score(y_test, result2)
print(accuracy1)
print("Random Forest:")
print(classification_report(y_test,result2))
print( confusion_matrix(y_test,result2))
#%% En iyi modelin kaydedilmesi
from sklearn.externals import joblib
joblib.dump(rfc, 'modell.pkl')





