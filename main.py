# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:03:12 2020

@author: ТОМА
"""

from statistics import *
from load_and_split import *
import pandas as pd


path_from="data/test.tsv"
path_to="data/test_proc.tsv"

def run_proc(path_from,path_to):

    df_test=split_columns(load(path_from))
    
    del df_test['features']
    #z-score нормализация
    df_test[df_test.filter(regex=r'feature_2_stand_{.').columns]=df_test.filter(regex=r'feature_2_stand_{.').apply(
                                        lambda x:znorm_feature(x),axis=0)
    
    #индекс i максимального
    #значения признака feature_2_{i} для данной вакансии
    df_test['max_feature_2_index']=df_test.filter(regex=r'feature_2_stand_{.').apply(
                                        lambda x:max_index(x),axis=1)
    
    #абсолютное отклонение признака с индексом max_feature_2_index от его
    #среднего значения
    df_test['max_feature_2_abs_mean_diff']=abs_diff(df_test)
    
    
    
    save(df_test,path_to)
    
if __name__ == '__main__':
    run_proc(path_from,path_to)    


