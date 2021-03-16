# -*- coding: utf-8 -*-
"""
------------------------------------------------------------
    Software:   PyCharm
    File Name:    config
    Description:   
  
    Author:  Phil
    Email:  furuoo@163.com
    Date:   2021/3/5 12:20
    Version:  3.8.1
"""
# --------------------------------------------------------------
#    Document Description：The file is a global setting of some parameters,
#    mainly divided into two aspects of OS indicators and DFS indicators,
#    in order to test the different special had of the two indicators respectively,
#    using the following comments into groups to modify.
#
# --------------------------------------------------------------

# Data sets for filtering, grouping and training
filename = "./data/bina.csv"

# Distinguish whether to expand the data using the SMOTE algorithm
# and control the branch by commenting out a particular string assignment.
Smote = '_smote'
# Smote = ''

# Names of all columns in the total data set
fullcolumns=['NO','病理号','住院号','姓名','Age','Gender (0:Male,1:Female)','Smoking (0:No, 1:Yes)',
             'Pathology','T','N','M','TNM-Stage','Chemotherapy (0:No, 1:Yes)','Radiotherapy (0:No, 1:Yes)',
             'CD3','CD4','CD8','PD-1','PD-L1 TILs','PD-L1 TC','PD-L2 TILs','PD-L2 TC','GAL 9 TIL','GAL 9 TC',
             'OX40L TIL','OX40L TC','HLA TIL','HLA TC','DFS','DFS Time (m)','OS','OS Time (m)']

# The names of the columns associated with the training result after removing personal information
usecols=['Age','Gender (0:Male,1:Female)',',Smoking (0:No, 1:Yes)','Pathology','T','N','M','TNM-Stage',
         'Chemotherapy (0:No, 1:Yes)','Radiotherapy (0:No, 1:Yes)','CD3','CD4','CD8','PD-1','PD-L1 TILs',
         'PD-L1 TC','PD-L2 TILs','PD-L2 TC','GAL 9 TIL','GAL 9 TC','OX40L TIL','OX40L TC','HLA TIL',
         'HLA TC','DFS','DFS Time (m)','OS','OS Time (m)']

# The following two sets of assignments are configurations for the OS and DFS cases,
# which control the operation of the other set of data by commenting out one set.

'''
x_cols=['TNM-Stage','CD4', 'PD-1', 'GAL 9 TIL','HLA TIL']
y_cols=['OS']
label, time, thred = 'OS', 'OS Time (m)', 24

'''

x_cols=['TNM-Stage','CD4', 'PD-1', 'GAL 9 TC']
y_cols=['DFS']
label, time, thred = 'DFS', 'DFS Time (m)', 24

# Name of the resampling results saving folder (distinguished by SMOTE algorithm)
filefolder = 'tmpdata'+Smote

