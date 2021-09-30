import pandas as pd
import csv
import streamlit as st

def valueSelect(df,col,value):
   
    uniqueValues=df[col].unique()
    o=df[col].value_counts()

    df_new=pd.DataFrame({col:[0], "Count":[0]})
    sum=0
    df.fillna(0)
    for val in uniqueValues:
        try:
            new_Row={col:val,"Count":o[val]}
            df_new=df_new.append(new_Row, ignore_index=True)
            sum=sum+o[val]
        except:
            pass

    df2=df.loc[(df[col] == value)]
    return df2

def checkKey(dict, key):      
    if key in dict:
        return True
    else:
        return False

def Checker(df,sidebars):
    dk=df
    k=pd.DataFrame()
    c=list(sidebars.keys())
    for column in c:
        cell_val=sidebars.get(column)
        if(len(cell_val)>=1):
            k=pd.DataFrame()
            for i in cell_val:
                temp=valueSelect(dk,column,str(i))
                k=k.append(temp)
            dk=k

    return dk
