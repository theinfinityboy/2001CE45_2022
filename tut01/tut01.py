import os
os.system("cls")
import pandas as pd
import numpy as np
#importing libraries
def check_octant(x,y,z):
    if x>=0 and y>=0 :
        o=1
    if x<0 and y>=0 :
        o=2
    if x<0 and y<0 :
        o=3
    if x>=0 and y<0 :
        o=4
    if z>=0 :
        return o
    if z<0 :
        return o*(-1)
def octact_identification(mod=5000):
    pass
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
datain['Octant']=np.nan
i=0
while i<29745:
    datain.loc[i,'Octant']=check_octant(datain.loc[i,'U-U_Avg'],datain.loc[i,'V-V_Avg'],datain.loc[i,'W-W_Avg'])
    i=i+1
print(datain)
mod=5000
octact_identification(mod)
