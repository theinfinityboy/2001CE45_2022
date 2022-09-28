import os
os.system("cls")
import pandas as pd
import numpy as np
import math
#importing libraries
os.chdir(r'C:\Users\pc\Documents\GitHub\2001CE45_2022\tut03')
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
        #till here quqdrant is checked
    if z>=0 :
        return o
    if z<0 :
        return o*(-1)
        #octant value returned as o
def octant_longest_subsequence_count():
    #complete code has been written in this(major portion)
    try:
        datain =  pd.read_excel('input_octant_longest_subsequence.xlsx') #reading input excel file and storing in variable datain as data input
        total_size=datain['U'].size      #size stored in variable
        U_Avg=datain['U'].mean()
        V_Avg=datain['V'].mean()
        W_Avg=datain['W'].mean()
        #mean value for each velocity value stored in variable
        datain['U_Avg']=''
        datain['V_Avg']=np.nan
        datain['W_Avg']=None
        #blank column naming average has been created in the three different ways
        datain.loc[0,'U_Avg']=U_Avg
        datain.loc[0,'V_Avg']=V_Avg
        datain.loc[0,'W_Avg']=W_Avg
        #storing the values of avg valocity in 1st row or 0 indexed row
        datain["U'=U-U_Avg"]=datain['U']-U_Avg
        datain["V'=V-V_Avg"]=datain['V']-V_Avg
        datain["W'=W-W_Avg"]=datain['W']-W_Avg
        #three more columns have been made and assigned value as V-Vavg.....corresponding name and corresponding columns
        datain['Octant']=np.nan #created a blank column named octant for which operation is to be done
        i=0 #initiating for loop variable
        while i<total_size: #loop is run for whole column size of input column file
            datain.loc[i,'Octant']=check_octant(datain.loc[i,"U'=U-U_Avg"],datain.loc[i,"V'=V-V_Avg"],datain.loc[i,"W'=W-W_Avg"])
            #octant column is assigned octant value after chehking value of octant by calling function
            i=i+1 #updating loop
        datain['']=np.nan
        datain['Octant Id']=np.nan
        datain['Longest Subsequence Length']=np.nan
        datain['Count']=np.nan
        datain.loc[0,'Octant Id']='+1'
        datain.loc[1,'Octant Id']='-1'
        datain.loc[2,'Octant Id']='+2'
        datain.loc[3,'Octant Id']='-2'
        datain.loc[4,'Octant Id']='+3'
        datain.loc[5,'Octant Id']='-3'
        datain.loc[6,'Octant Id']='+4'
        datain.loc[7,'Octant Id']='-4'
        
        try:
            datain.to_excel('output_octant_longest_subsequence.xlsx',index=False)# it makes a csv file with the name given in 'quote'
            print("Your desired output file is ready!!! Please Check!")
        except:
            print("the filename which you try to overwrite..Is it open or what? if it is open I cannot overwrite..please close")
                #index = false do not make make columns for index values as we have no requirement of it in this case    
    except FileNotFoundError:
        print("Hey...filename inputed by user is not found")
    

###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


octant_longest_subsequence_count()