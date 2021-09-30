import streamlit as st
import pandas as pd
from functions import valueSelect
from functions import checkKey
from functions import Checker
st.write("""# Data""")

df = pd.read_excel("Combined data UC-I_AHP GM_with intersectional.xlsm")
df_2=pd.read_excel("1-UC-I FCG+ ZTM_201112_Updated.xlsx")
k1=df
k2=df_2
sidebars = {}
listOfSide=['Doyouconsideryourselftoliveina','Whatisthehighestlevelofeducationyouhaveachieved','Whatisyouraverageyearlyincome','Inyourfamilyunitdoyoulivewithanydependentpersonchildrenorelderl','Whatisyourhouseholdtype','Doyoutravelonaweeklybasiswithadependentpersonchildrenelderlycar','Whatisyourprofessionalstatus','Whichreligiousgroupdoyoumostidentifywith','Inemploymentdoyou','Doyoucurrentlyhaveanillnessimpairmentordisabilitywhichaffectsho','Whatisyourmaincitizenship', 'Doyouidentifyas','Areyoucurrentlyworkingintransport']
count=0
for y in listOfSide:
    ucolumns=list(df[y].unique())
    ucolumns.extend(list(df_2[y].unique()))
    sidebars[y]=st.sidebar.multiselect('Filter '+y, ucolumns)   


if bool(sidebars):
    L = [df[k].isin(v) if isinstance(v, list) 
        else df[k].eq(v) 
        for k, v in sidebars.items() if k in df.columns]
    
    k1=Checker(df,sidebars)
    k2=Checker(df,sidebars)

    # c=list(sidebars.keys())

    # for key in listOfSide:
    #     if checkKey(sidebars,key):
    #         column=c[count]
    #         try:
    #             st.empty()
    #             cell_val=sidebars.get(column)
    #             # k1=valueSelect(df,column,str(cell_val[0])) 
    #             # k2=valueSelect(df,column,str(cell_val[0]))
    #             # st.write(df)
                
    #         except:
    #             pass 
    #     else:
    #         pass
    #     count=count+1

st.write("""Combined data""")
st.dataframe(k1)
st.write("""UC-1""")
st.write(k2)

# 'ResidentialDetailsWheredoyoucurrentlylive', 'Whatagebracketareyou', 'Ifyeswhichtransportsectordoyouworkin','Doyouconsideryourselftobe',