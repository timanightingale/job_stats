# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:20:12 2020

@author: ТОМА
"""

import pandas as pd

def load(path):
    
    df=pd.read_csv(path,sep='\t')
    return df
    
def save(df,path):
    
    df.to_csv(path,sep='\t',index=False)
    
    return df
def split_columns(df):
    num=df['features'].iloc[0].split(',')[0]
    columns=['feature_%s_stand_{%s}'%(num,i) for i in range(256)]
    values=df['features'].apply(lambda x:x.split(',')[1:]).tolist()
    df_split=pd.DataFrame(data=values,
                     columns=columns).astype(int)
    
    df=pd.concat([df,df_split],axis=1)
    
    return df


