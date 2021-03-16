# -*- coding: utf-8 -*-
"""
------------------------------------------------------------
    Software:   PyCharm
    File Name:    num_count
    Description:   
  
    Author:  Phil
    Email:  furuoo@163.com
    Date:   2021/3/7 21:20
    Version:  3.8.1
"""
# --------------------------------------------------------------
#    Document Description:
#       Statistics on the percentage of expanded data using the SMOTE algorithm
#
# --------------------------------------------------------------

import pandas as pd
from data_select import data_select
from config import filename,fullcolumns,x_cols,y_cols
from imblearn.over_sampling import SMOTE  # Import SMOTE algorithm module


data = pd.read_csv(filename, encoding='utf-8', usecols=fullcolumns)
len1 = len(data)
labels = ['OS', 'DFS']
threds = [12, 24, 36, 60]
print('label time original selected smote')

for label in labels:
    for thred in threds:
        time = label+' Time (m)'
        index1 = data_select(data, label, 1, time, '<', thred)
        index2 = data_select(data, label, 0, time, '>=', thred)

        df1 = data[fullcolumns][index1]
        df2 = data[fullcolumns][index2]

        df=pd.concat([df1,df2])

        # Divide the data set and test set
        X = df[x_cols]
        y = df[y_cols]
        len2 = len(y)

        # Processing unbalanced data, oversampling (oversampling) with SMOTE algorithm module
        sm = SMOTE(random_state=42)    # Methods for handling oversampling
        X, y = sm.fit_sample(X, y)
        len3 = len(y)

        print('{la:5} {th:4} {len1:8} {len2:8}{len3:5}'.format(la=label, th=thred,len1=len1,len2=len2,len3=len3))

