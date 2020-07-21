# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:42:37 2020

@author: ТОМА
"""


import numpy as np

def znorm_feature(col):
    mean=col.mean()
    std=col.std()
    
    z_norm=(col-mean)/std
    return z_norm

def max_index(row):
    i=np.argmax(row.values)
    return i
    
def abs_diff(df):
    mean_dict={i:val for i, val in zip(range(256),df.filter(regex=r'feature_2_stand_{.').mean(axis=0).values.tolist())}  
    diff=np.abs(
        df['max_feature_2_index'].map(mean_dict)-df.filter(regex=r'feature_2_stand_{.').max(axis=1)
        ).astype(int)
    
    return diff
