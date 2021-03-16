# -*- coding: utf-8 -*-
"""
------------------------------------------------------------
    Software:   PyCharm
    File Name:    bina_RF_XGB.py
    Description:   
  
    Author:  Phil
    Email:  furuoo@163.com
    Date:   2021/2/28 9:57
    Version:  3.8.1
"""

# --------------------------------------------------------------
#    Document Description：Training and scoring between random forest
#    and XGBoost algorithms using 0-1 binary data after cox analysis.
#
# --------------------------------------------------------------

from config import x_cols, y_cols, filefolder, Smote
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, roc_auc_score
from xgboost import XGBClassifier

catagory = y_cols[0]

names=['month', 'No']
names.extend(x_cols)
names.extend(['score','F1','AUC'])
data=[]

for month in [12,24,36,60]:
    print('\n-------------------------------------------------------------------')
    for i in range(100):
        tmp = []
        print('month = {month}, No = {i}'.format(month=month, i=i+1))
        tmp.append(month)
        tmp.append(i+1)
        train_file = filefolder+'/'+catagory+'_'+str(month)+'_'+str(i+1)+'_train'+Smote+'.csv'
        test_file = filefolder+'/'+catagory+'_'+str(month)+'_'+str(i+1)+'_test'+Smote+'.csv'
        df_train = pd.read_csv(train_file, encoding='utf-8')
        df_test = pd.read_csv(test_file, encoding='utf-8')
        X_train = df_train[x_cols]
        y_train = df_train[y_cols].values.ravel()
        X_test = df_test[x_cols]
        y_test = df_test[y_cols].values.ravel()

        # Methods for machine learning with random forests
        rf = RandomForestRegressor(n_estimators=50, max_depth=5, random_state=2021)
        # The hyperparameter random_state = 2021 is taken here to ensure the reproducibility
        # of the experimental results.
        rf.fit(X_train, y_train)
        print("rf FI:",rf.feature_importances_)
        FI = list(rf.feature_importances_)
        tmp.extend(FI)
        y_pred = np.round(rf.predict(X_test))
        rf_score = accuracy_score(y_test, y_pred)
        # Accuracy: Accuracy is the proportion of correctly classified samples to the total number of samples
        tmp.append(rf_score)

        rf_f1 = metrics.f1_score(y_test, y_pred)
        tmp.append(rf_f1)

        rf_auc = roc_auc_score(y_test, y_pred)  # rf_auc值
        tmp.append(rf_auc)

        print('rf score F1 auc:', rf_score, rf_f1, rf_auc)

        # XGBoost for machine learning
        XGB = XGBClassifier()
        XGB.fit(X_train, y_train)
        print("XGB FT", XGB.feature_importances_)

        y_pred = XGB.predict(X_test)

        XGB_score = accuracy_score(y_test, y_pred)
        # Accuracy: Accuracy is the proportion of correctly classified samples to the total number of samples
        XGB_recall = metrics.recall_score(y_test, y_pred)  # value of XGB_recall
        XGB_f1_score = metrics.f1_score(y_test, y_pred)  # value of XGB_f1_score
        XGB_auc = roc_auc_score(y_test, y_pred)  # value of XGB_auc
        print('XGB score recall f1 auc:',XGB_score,XGB_recall,XGB_f1_score,XGB_auc)
        print('\n')

        data.append(tmp)

    print("Valid samples'number is {num} after {time} month".format(num=len(df_train) + len(df_test), time=month))


# list --> dataframe
df = pd.DataFrame(data, columns=names)
print(df.head(5))
df.to_csv('result/'+catagory+'_result'+Smote+'.csv', index=False)




