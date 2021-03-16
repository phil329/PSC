# -*- coding: utf-8 -*-
"""
------------------------------------------------------------
    Software:   PyCharm
    File Name:    tmp_data_sample
    Description:   
  
    Author:  Phil
    Email:  furuoo@163.com
    Date:   2021/3/5 12:03
    Version:  3.8.1
"""
# --------------------------------------------------------------
#    Document Description:Randomly generate 100 groups of oversampling data,
#    in order to ensure that the experimental data can be reproduced,
#    set the random sampling Random_state = i
#    (i is the serial number of the compilation group)
#
# --------------------------------------------------------------

import pandas as pd
import os
from data_select import data_select
from config import filename,fullcolumns,x_cols,y_cols,label,time,thred,filefolder,Smote
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split


data = pd.read_csv(filename, encoding='utf-8', usecols=fullcolumns)
print(data.head(5))


index1 = data_select(data, label, 1, time, '<', thred)
index2 = data_select(data, label, 0, time, '>=', thred)

df1 = data[fullcolumns][index1]
df2 = data[fullcolumns][index2]

df=pd.concat([df1,df2])

# Divide the data set and test set
X = df[x_cols]
y = df[y_cols]
print("Number of valid samples obtained after screening:", len(y))

# Processing unbalanced data, oversampling (oversampling) with SMOTE algorithm module
sm = SMOTE(random_state=42)    # Methods for handling oversampling
X, y = sm.fit_sample(X, y)
print("Total number of samples expanded by SMOTE algorithm:", len(y))


if not os.path.exists(filefolder):
    os.makedirs(filefolder)


for i in range(100):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=i)
    df_train = pd.concat([X_train, y_train], axis=1)
    df_test = pd.concat([X_test,y_test],axis=1)
    names = x_cols.copy()
    names.extend(y_cols)

    df_train.to_csv(filefolder+'/{label}_{time}_{no}_train{smote}.csv'.format(label=label, time=thred, no=i+1,smote=Smote),
                    columns=names,index=False)
    df_test.to_csv(filefolder+'/{label}_{time}_{no}_test{smote}.csv'.format(label=label, time=thred, no=i+1,smote=Smote),
                   columns=names,index=False)
    print(i+1)


