# -*- coding: utf-8 -*-
"""
------------------------------------------------------------
    Software:   PyCharm
    File Name:    RandomForestBestPara
    Description:   
  
    Author:  Phil
    Email:  furuoo@163.com
    Date:   2021/3/7 22:08
    Version:  3.8.1
"""
# --------------------------------------------------------------
#    Document Description:Determine the optimal parameters of
#    the random forest using the grid search method.
#
# --------------------------------------------------------------


import time
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from config import x_cols, y_cols
from sklearn.metrics import accuracy_score, roc_auc_score

if __name__ == '__main__':
    # user_model cv
    #Maintain the same data between the model training sample and the reference sample before tuning

    file1 = 'tmpdata_smote/DFS_36_15_train_smote.csv'
    file2 = 'tmpdata_smote/DFS_36_15_test_smote.csv'
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    max_score = 0
    max_auc = 0

    print('--------------Start adjusting the parameters---------------')
    start = time.time()
    X_train = df1[x_cols]
    y_train = df1[y_cols].values.ravel()
    X_test = df2[x_cols]
    y_test = df2[y_cols]

    n_estimators = list(range(1,21))
    max_depths = [2, 3, 4, 5, 6]
    bootstraps = [False,True]
    max_features =['auto','sqrt','log2','None']


    for n_estimator in n_estimators:
        for max_depth in max_depths:
            for bootstrap in bootstraps:
                rf = RandomForestRegressor(
                    n_estimators=n_estimator,
                    random_state=2021,
                    max_depth=max_depth,
                    bootstrap=bootstrap,
                )
                rf.fit(X_train,y_train)

                y_pred = np.round(rf.predict(X_test))
                score = accuracy_score(y_pred,y_test)
                auc = roc_auc_score(y_pred,y_test)
                if auc > max_auc or score >max_score:
                    max_score = score
                    max_auc = auc
                    print(n_estimator,max_depth,bootstrap,score,auc)

    print('Time to adjust parameters : %s'%(time.time()-start))


