import os
os.system("cls")
import pandas as pd
import numpy as np
import math
#importing libraries
def check_octant(x,y,z):
    #this function will check for the octant
        #first it will check for quadrant
        #then it will update it for the octant by looking the z values(w-w_avg for the main data)
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
    datain =  pd.read_csv('octant_input.csv')
    total_size=datain['U'].size
    U_Avg=datain['U'].mean()
    V_Avg=datain['V'].mean()
    W_Avg=datain['W'].mean()
    datain['U_Avg']=''
    datain['V_Avg']=np.nan
    datain['W_Avg']=None
    datain.loc[0,'U_Avg']=U_Avg
    datain.loc[0,'V_Avg']=V_Avg
    datain.loc[0,'W_Avg']=W_Avg
    datain['U-U_Avg']=datain['U']-U_Avg
    datain['V-V_Avg']=datain['V']-V_Avg
    datain['W-W_Avg']=datain['W']-W_Avg
    datain['Octant']=np.nan
    i=0
    
    while i<total_size:
        datain.loc[i,'Octant']=check_octant(datain.loc[i,'U-U_Avg'],datain.loc[i,'V-V_Avg'],datain.loc[i,'W-W_Avg'])
        i=i+1
    datain['']=np.nan
    datain.loc[1,'']="User Input"
    datain['Octant Id']=np.nan
    datain['1']=np.nan
    datain['-1']=np.nan
    datain['2']=np.nan
    datain['-2']=np.nan
    datain['3']=np.nan
    datain['-3']=np.nan
    datain['4']=np.nan
    datain['-4']=np.nan
    datain.loc[0,'Octant Id']="Overall Count"
    datain.loc[1,'Octant Id']="mod {}".format(mod)
    noi = math.ceil(total_size/mod)
    i=0
    op1=0
    on1=0
    op2=0
    on2=0
    op3=0
    on3=0
    op4=0
    on4=0
    while i<noi:
        if(i+1)*mod>total_size:
            u=total_size-1
        else:
            u=(i+1)*mod-1
        l=i*mod
        datain.loc[i+2,'Octant Id']="{}-{}".format(l,u)
        j=0
        p1=0
        n1=0
        p2=0
        n2=0
        p3=0
        n3=0
        p4=0
        n4=0
        while j<mod:
            
            pos =(i*mod)+j
            if pos>=total_size:
                break
            else:
                if datain.loc[pos,'Octant']==1:
                    p1=p1+1
                elif datain.loc[pos,'Octant']==-1:
                    n1=n1+1
                elif datain.loc[pos,'Octant']==2:
                    p2=p2+1
                elif datain.loc[pos,'Octant']==-2:
                    n2=n2+1
                elif datain.loc[pos,'Octant']==3:
                    p3=3+1
                elif datain.loc[pos,'Octant']==-3:
                    n3=n3+1
                elif datain.loc[pos,'Octant']==4:
                    p4=p4+1
                elif datain.loc[pos,'Octant']==-4:
                    n4=n4+1 
            j=j+1
        op1=op1+p1
        on1=on1+n1
        op2=op2+p2
        on2=on2+n2
        op3=op3+p3
        on3=on3+n3
        op4=op4+p4
        on4=on4+n4
        datain.loc[i+2,'1']=p1
        datain.loc[i+2,'-1']=n1
        datain.loc[i+2,'2']=p2
        datain.loc[i+2,'-2']=n2
        datain.loc[i+2,'3']=p3
        datain.loc[i+2,'-3']=n3
        datain.loc[i+2,'4']=p4
        datain.loc[i+2,'-4']=n4
        i=i+1
    datain.loc[0,'1']=op1
    datain.loc[0,'-1']=on1
    datain.loc[0,'2']=op2
    datain.loc[0,'-2']=on2
    datain.loc[0,'3']=op3
    datain.loc[0,'-3']=on3
    datain.loc[0,'4']=op4
    datain.loc[0,'-4']=on4
    datain.to_csv('octant_output.csv',index=False)
mod=5000
octact_identification(mod)

