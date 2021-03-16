# -*- coding: utf-8 -*-
"""
------------------------------------------------------------
    Software:   PyCharm
    File Name:    data_select
    Description:   
  
    Author:  Phil
    Email:  furuoo@163.com
    Date:   2021/3/5 11:56
    Version:  3.8.1
"""
# --------------------------------------------------------------
#    Document Description:The data filtering function used when handling deleted data.
#    Sort and filter by time, tag information
#    
# --------------------------------------------------------------
import pandas as pd

def data_select(df,label, label_va, time, comp, thre):
    '''
    df:original dataframe
    label:OS
    label_va:1 or 0
    time:OS Time (m)
    comp:'<',   '>',    '<=',   '>=',   '==',   '!='
    thre:12 or others
    return: index of selected item
    '''

    ix1 = (df[label] ==label_va)
    if comp == '<':
        ix2 = (df[time] < thre)
    elif comp == '>':
        ix2 = (df[time] > thre)
    elif comp == '>=':
        ix2 = (df[time] >= thre)
    elif comp == '<':
        ix2 = (df[time] <= thre)
    elif comp == '==':
        ix2 = (df[time] == thre)
    elif comp == '!=':
        ix2 = (df[time] != thre)
    ix = []
    for i in range(len(ix1)):
        # print(ix1[i],ix2[i])
        if ix1[i] == True and ix2[i] == True:
            ix.append(True)
        else:
            ix.append(False)
    ix = pd.Series(ix)
    return ix
