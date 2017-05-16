#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np

import numpy.lib.recfunctions as rfn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sqlalchemy import create_engine

path1 = 'table1.csv'
path2 = 'table2.csv'
dbconnector='mysql+mysqlconnector://root:root@localhost/randomforst'

def datatype(s):
    it={'H':0,'L':1,'N':2}
    return it[s.strip()]


def getdataframe():
    engine = create_engine(dbconnector)
    df1=pd.read_csv(path1, index_col='ID')
    df2=pd.read_csv(path2, index_col='ID',converters={1: datatype, 2:datatype,3:datatype,4:datatype,5:datatype,6:datatype,7:datatype})
    df=pd.merge(df2,df1, right_index=True,left_index=True)
    #
    #here is database write, if you want to speed up please delete the line below
    df.to_sql("sample",engine,if_exists='replace')
    return df

def trainmodel(data, target,model):
    rf_clf=model.fit(data, target)
    return rf_clf

def predictrate(data, target, model):
    r_hat=model.predict(data)
    re = (r_hat == target)
    return np.mean(re)


def work():
    df=getdataframe()
    data,target=np.split(df.values, (10,), axis=1)
    x_train, x_test, y_train, y_test = train_test_split(data, target.reshape(-1), test_size=0.3, random_state=1)
    model=RandomForestClassifier(n_estimators=200, max_features=4,criterion='gini')
    rf_clf=model.fit(x_train, y_train.reshape(-1))
    re=predictrate(x_test, y_test.reshape(-1), rf_clf)
    return re

if __name__ == "__main__":
    df=getdataframe()
    data,target=np.split(df.values, (10,), axis=1)
    x_train, x_test, y_train, y_test = train_test_split(data, target.reshape(-1), test_size=0.3, random_state=1)
    model=RandomForestClassifier(n_estimators=200, max_features=4,criterion='gini')
    rf_clf=model.fit(x_train, y_train.reshape(-1))
    re=predictrate(x_test, y_test.reshape(-1), rf_clf)
