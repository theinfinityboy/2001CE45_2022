import os
os.system("cls")
import pandas as pd
import numpy as np
#importing libraries

def octact_identification(mod=5000):
    datain =  pd.read_csv(r'C:\Users\pc\Documents\GitHub\2001CE45_2022\tut01\octant_input.csv')
    U_Avg=datain['U'].mean()
    V_Avg=datain['V'].mean()
    W_Avg=datain['W'].mean()
    datain['U_Avg']=''
    datain['V_Avg']=np.nan
    datain['W_Avg']=None
    datain.loc[0,'U_Avg']=U_Avg
    datain.loc[0,'V_Avg']=V_Avg
    datain.loc[0,'W_Avg']=W_Avg
    # datain.drop_duplicates(subset=['U_Avg'],inplace=True)
    # datain.drop_duplicates(subset=['V_Avg'],inplace=True)
    # datain.drop_duplicates(subset=['W_Avg'],inplace=True)
    datain['U-U_Avg']=datain['U']-U_Avg
    datain['V-V_Avg']=datain['V']-V_Avg
    datain['W-W_Avg']=datain['W']-W_Avg
    print(datain)
    


mod=5000
octact_identification(mod)