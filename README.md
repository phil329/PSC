# **An Immune-based Risk-stratification System for Predicting Prognosis in Pulmonary Sarcomatoid Carcinoma (PSC)** 

## The Environment

- Windows 10 64bit
- Python 3.8.1
- Pandas == 1.0.1
- sklearn == 0.23.2
- xgboost == 1.1.0

## Document Directory

│   README.md
├─data
│      bina.csv
├─result
├─src
│      bina_RF_XGB.py
│      config.py
│      data_select.py
│      LifeLinesTest.py
│      num_count.py
│      RandomForestBestPara.py
│      tmp_data_sample.py
├─tmpdata
│      OS_12_3_train.csv
│      readme.txt
│      
└─tmpdata_smote
        OS_12_2_train_smote.csv
        readme.txt

## Folder Description

### data

The data folder holds the raw data bina.csv.

### src

The source files are placed in the src folder. Please refer to the comments and file descriptions in the file for specific file descriptions.

### result

The result folder holds the results of data processing and is divided into two categories of processing data, OS and DFS.

### tmpdata & tmpdata_smote

These two folders hold the resampled respective 100 sets of data, distinguished by time points and different labels.

## About us

Any questions or errors please contact us with furuoo@163.com



