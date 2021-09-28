import pandas as pd
import csv
import streamlit as st

def valueSelect(df,col,value):
    # print(value)
   
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
    
# data = pd.read_excel("Combined data UC-I_AHP GM_with intersectional.xlsm")
# data2=valueSelect(data,'Inyourfamilyunitdoyoulivewithanydependentpersonchildrenorelderl','Preschool age children (under 5 years)')
# print(data2)
# data3=valueSelect(data2,'Doyouconsideryourselftoliveina','An urban environment')
# print(data3)
# data4=valueSelect(data3,'Whatisyourprofessionalstatus','Paid employment')
# print(data4)

# data5=valueSelect(data4,'Whichreligiousgroupdoyoumostidentifywith','Christian (all denominations)')
# print(data5)
def checkKey(dict, key):      
    if key in dict:
        return True
    else:
        return False