#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy.lib.recfunctions as rfn
from sklearn.ensemble import RandomForestClassifier

def datatype(s):
    #﻿it={'ID':0,'VAR1':1,'VAR2':2,'VAR3':3,'VAR4':4,'VAR5':5,'VAR6':6,'VAR7':7,'VAR8':8,'VAR9':9,'VAR10':9,'OUTCOME':10}
    it={'N':0,'L':1,'H':2}
    return it[str(s.strip(), 'utf-8')]

if __name__ == "__main__":
    path1 = 'table1.csv'
    path2 = 'table2.csv'
    data1 = np.loadtxt(path1, dtype=[('id', int),('VAR1', int),('VAR2', int),('VAR3', float),('OUTCOME', int)], delimiter=',', skiprows=1)
    data2 = np.loadtxt(path2, dtype=[('id', int),('VAR4', int),('VAR5', int),('VAR6', int),('VAR7', int),('VAR8', int),('VAR9', int)],delimiter=',', skiprows=1,converters={1: datatype, 2:datatype,3:datatype,4:datatype,5:datatype,6:datatype})
    data =rfn.join_by('id', data1,data2, jointype='inner' usemask=False)
