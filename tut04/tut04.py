import os
os.system("cls")
import pandas as pd
import numpy as np
import math
#importing libraries
os.chdir(r'C:\Users\pc\Documents\GitHub\2001CE45_2022\tut04')
#current directory location
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
def octant_longest_subsequence_count_with_range():
    #complete code has been written in this(major portion)
    try:
        datain =  pd.read_excel('input_octant_longest_subsequence_with_range.xlsx') #reading input excel file and storing in variable datain as data input
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
        #till here matrix has been made now we have to fill the values in the dataframe
        scp1=scn1=scp2=scn2=scp3=scn3=scp4=scn4=0 #made variable for subsequent positive and negative count
        cp1=cn1=cp2=cn2=cp3=cn3=cp4=cn4=0 #made variables for count the appearance of subsequent count
        listp1=[]
        listn1=[]
        listp2=[]
        listn2=[]
        listp3=[]
        listn3=[]
        listp4=[]
        listn4=[]
        #empty list made to use it later for time range printing

        for i in range(0,total_size):
            if(datain.loc[i,'Octant']==1): 
                count=0 #initiated local variable which will help in updating sc#@(p/n)(1/2/3/4)
                while (datain.loc[i,'Octant']==1): #loop for checking appearance of velocity in octant
                    count+=1 #updating count
                    i+=1 #updating rows for checking continuity in a octant
                    if(i>=total_size):
                        break #this is because we have only rows upto index total size-1 and .loc func will unable to access the rows which actually does not exist
                if(count>scp1):
                    scp1=count #updating subsequent longest  count 
                    cp1=1 #assigning value as 1 because of new longest subsequent count
                    listp1.clear() #list has been cleared in case it has any previous element which shouldn't in case of if case
                    listp1.append(i-1) #storing index of upper bound(inclusive) which will help later
                elif (count==scp1):
                    cp1+=1 #updating count value of subsequent longest count in case of same subs. long. count
                    listp1.append(i-1) #storing index of upper bound(inclusive) which will help later
                    ################
                    #after this same code has been done for all the octanct type occurence so no comment needed till code line 166
            elif(datain.loc[i,'Octant']==-1):
                count=0
                while (datain.loc[i,'Octant']==-1):
                    count+=1 #explained in +ve 1 coode writing all step is same as that
                    i+=1
                    if(i>=total_size):
                        break
                if(count>scn1):
                    scn1=count
                    cn1=1
                    listn1.clear()
                    listn1.append(i-1) #storing index of upper bound(inclusive) which will help later
                elif (count==scn1):
                    cn1+=1
                    listn1.append(i-1) #storing index of upper bound(inclusive) which will help later
            elif(datain.loc[i,'Octant']==2):
                count=0
                while (datain.loc[i,'Octant']==2):
                    count+=1
                    i+=1
                    if(i>=total_size):
                        break
                if(count>scp2):
                    scp2=count
                    cp2=1
                    listp2.clear()
                    listp2.append(i-1) #storing index of upper bound(inclusive) which will help later
                elif (count==scp2):
                    cp2+=1
                    listp2.append(i-1) #storing index of upper bound(inclusive) which will help later
            elif(datain.loc[i,'Octant']==-2):
                count=0
                while (datain.loc[i,'Octant']==-2):
                    count+=1
                    i+=1
                    if(i>=total_size):
                        break
                if(count>scn2):
                    scn2=count
                    cn2=1
                    listn2.clear()
                    listn2.append(i-1) #storing index of upper bound(inclusive) which will help later
                elif (count==scn2):
                    cn2+=1
                    listn2.append(i-1) #storing index of upper bound(inclusive) which will help later
            elif(datain.loc[i,'Octant']==3):
                count=0
                while (datain.loc[i,'Octant']==3):
                    count+=1
                    i+=1
                    if(i>=total_size):
                        break
                if(count>scp3):
                    scp3=count
                    cp3=1
                    listp3.clear()
                    listp3.append(i-1) #storing index of upper bound(inclusive) which will help later
                elif (count==scp3):
                    cp3+=1
                    listp3.append(i-1) #storing index of upper bound(inclusive) which will help later
            elif(datain.loc[i,'Octant']==-3):
                count=0
                while (datain.loc[i,'Octant']==-3):
                    count+=1
                    i+=1
                    if(i>=total_size):
                        break
                if(count>scn3):
                    scn3=count
                    cn3=1
                    listn3.clear()
                    listn3.append(i-1) #storing index of upper bound(inclusive) which will help later
                elif (count==scn3):
                    cn3+=1
                    listn3.append(i-1) #storing index of upper bound(inclusive) which will help later
            elif(datain.loc[i,'Octant']==4):
                count=0
                while (datain.loc[i,'Octant']==4):
                    count+=1
                    i+=1
                    if(i>=total_size):
                        break
                if(count>scp4):
                    scp4=count
                    cp4=1
                    listp4.clear()
                    listp4.append(i-1) #storing index of upper bound(inclusive) which will help later
                elif (count==scp4):
                    cp4+=1
                    listp4.append(i-1) #storing index of upper bound(inclusive) which will help later
            elif(datain.loc[i,'Octant']==-4):
                count=0
                while (datain.loc[i,'Octant']==-4):
                    count+=1
                    i+=1
                    if(i>=total_size):
                        break
                if(count>scn4):
                    scn4=count
                    cn4=1
                    listn4.clear()
                    listn4.append(i-1) #storing index of upper bound(inclusive) which will help later
                elif (count==scn4):
                    cn4+=1
                    listn4.append(i-1) #storing index of upper bound(inclusive) which will help later
            i=i-1 #this substraction in the row has been done because of an extra addition of row while checking the repitition
            #in the octant and in case of failing of repitition condition row will gone to another position already
            #we know about loop condition after each iteration it increases its loop by doing one iteration operation
            #so on adding 1 we will actually jump two row but we need to jump only one row
            #1 has been substracted to have no skipped row to get correct result
            ###till here done#######
        datain.loc[0,'Longest Subsequence Length']=scp1 #assigning longest subsequent value corresponding to positive 1 octant value
        datain.loc[0,'Count']=cp1 #assigning count of longest subs. value corresponding to +ve 1
        datain.loc[1,'Longest Subsequence Length']=scn1
        datain.loc[1,'Count']=cn1 #assigning count of longest subs. value corresponding to -ve 1
        datain.loc[2,'Longest Subsequence Length']=scp2
        datain.loc[2,'Count']=cp2 #assigning count of longest subs. value corresponding to +ve 2
        datain.loc[3,'Longest Subsequence Length']=scn2
        datain.loc[3,'Count']=cn2 #assigning count of longest subs. value corresponding to -ve 2
        datain.loc[4,'Longest Subsequence Length']=scp3
        datain.loc[4,'Count']=cp3 #assigning count of longest subs. value corresponding to +ve 3
        datain.loc[5,'Longest Subsequence Length']=scn3
        datain.loc[5,'Count']=cn3 #assigning count of longest subs. value corresponding to -ve 3
        datain.loc[6,'Longest Subsequence Length']=scp4
        datain.loc[6,'Count']=cp4 #assigning count of longest subs. value corresponding to +ve 4
        datain.loc[7,'Longest Subsequence Length']=scn4
        datain.loc[7,'Count']=cn4 #assigning count of longest subs. value corresponding to -ve 4



        #till here done now working  for range values and indexe range of longest subsequence count
        datain[' ']=np.nan #created blank column with no name as asked in the excel file
        datain['Octant Id2']=np.nan
        datain['Longest Subsquence Length2']=np.nan
        datain['Count2']=np.nan
        #making desired matrix for +1
        datain.loc[0,'Octant Id2']='+1'
        datain.loc[1,'Octant Id2']='Time'
        datain.loc[0,'Longest Subsquence Length2']=scp1
        datain.loc[1,'Longest Subsquence Length2']='From'
        datain.loc[0,'Count2']=cp1
        datain.loc[1,'Count2']='To'
        #making desired matrix for filling the time range of -1
        datain.loc[2+cp1,'Octant Id2']='-1'
        datain.loc[2+cp1,'Longest Subsquence Length2']=scn1
        datain.loc[2+cp1,'Count2']=cn1
        datain.loc[3+cp1,'Octant Id2']='Time'
        datain.loc[3+cp1,'Longest Subsquence Length2']='From'
        datain.loc[3+cp1,'Count2']='To'
        #making desired matrix for filling the time range of +2
        datain.loc[4+cp1+cn1,'Octant Id2']='+2'
        datain.loc[4+cp1+cn1,'Longest Subsquence Length2']=scp2
        datain.loc[4+cp1+cn1,'Count2']=cp2
        datain.loc[5+cp1+cn1,'Octant Id2']='Time'
        datain.loc[5+cp1+cn1,'Longest Subsquence Length2']='From'
        datain.loc[5+cp1+cn1,'Count2']='To'
        #making desired matrix for filling the time range of -2
        datain.loc[6+cp1+cn1+cp2,'Octant Id2']='-2'
        datain.loc[6+cp1+cn1+cp2,'Longest Subsquence Length2']=scn2
        datain.loc[6+cp1+cn1+cp2,'Count2']=cn2
        datain.loc[7+cp1+cn1+cp2,'Octant Id2']='Time'
        datain.loc[7+cp1+cn1+cp2,'Longest Subsquence Length2']='From'
        datain.loc[7+cp1+cn1+cp2,'Count2']='To'
        #making desired matrix for filling the time range of +3
        datain.loc[8+cp1+cn1+cp2+cn2,'Octant Id2']='+3'
        datain.loc[8+cp1+cn1+cp2+cn2,'Longest Subsquence Length2']=scp3
        datain.loc[8+cp1+cn1+cp2+cn2,'Count2']=cp3
        datain.loc[9+cp1+cn1+cp2+cn2,'Octant Id2']='Time'
        datain.loc[9+cp1+cn1+cp2+cn2,'Longest Subsquence Length2']='From'
        datain.loc[9+cp1+cn1+cp2+cn2,'Count2']='To'
        #making desired matrix for filling the time range of -3
        datain.loc[10+cp1+cn1+cp2+cn2+cp3,'Octant Id2']='-3'
        datain.loc[10+cp1+cn1+cp2+cn2+cp3,'Longest Subsquence Length2']=scn3
        datain.loc[10+cp1+cn1+cp2+cn2+cp3,'Count2']=cn3
        datain.loc[11+cp1+cn1+cp2+cn2+cp3,'Octant Id2']='Time'
        datain.loc[11+cp1+cn1+cp2+cn2+cp3,'Longest Subsquence Length2']='From'
        datain.loc[11+cp1+cn1+cp2+cn2+cp3,'Count2']='To'
        #making desired matrix for filling the time range of +4
        datain.loc[12+cp1+cn1+cp2+cn2+cp3+cn3,'Octant Id2']='+4'
        datain.loc[12+cp1+cn1+cp2+cn2+cp3+cn3,'Longest Subsquence Length2']=scp4
        datain.loc[12+cp1+cn1+cp2+cn2+cp3+cn3,'Count2']=cp4
        datain.loc[13+cp1+cn1+cp2+cn2+cp3+cn3,'Octant Id2']='Time'
        datain.loc[13+cp1+cn1+cp2+cn2+cp3+cn3,'Longest Subsquence Length2']='From'
        datain.loc[13+cp1+cn1+cp2+cn2+cp3+cn3,'Count2']='To'
        #making desired matrix for filling the time range of -4
        datain.loc[14+cp1+cn1+cp2+cn2+cp3+cn3+cp4,'Octant Id2']='-4'
        datain.loc[14+cp1+cn1+cp2+cn2+cp3+cn3+cp4,'Longest Subsquence Length2']=scn4
        datain.loc[14+cp1+cn1+cp2+cn2+cp3+cn3+cp4,'Count2']=cn4
        datain.loc[15+cp1+cn1+cp2+cn2+cp3+cn3+cp4,'Octant Id2']='Time'
        datain.loc[15+cp1+cn1+cp2+cn2+cp3+cn3+cp4,'Longest Subsquence Length2']='From'
        datain.loc[15+cp1+cn1+cp2+cn2+cp3+cn3+cp4,'Count2']='To'

        ##############################################################################
        #till here matrix done
        #now working for matrix filling
        for c in range (0,cp1):
            datain.loc[2+c,'Count2']=datain.at[listp1[c],'Time'] #upper limit time i.e. to
            datain.loc[2+c,'Longest Subsquence Length2']=datain.at[1+listp1[c]-scp1,'Time'] #lower limit time i. e. from
        for c in range (0,cn1):
            datain.loc[4+cp1+c,'Count2']=datain.at[listn1[c],'Time'] #upper limit time i.e. to
            datain.loc[4+cp1+c,'Longest Subsquence Length2']=datain.at[1+listn1[c]-scn1,'Time'] #lower limit time i. e. from
        for c in range (0,cp2):
            datain.loc[6+cp1+cn1+c,'Count2']=datain.at[listp2[c],'Time'] #upper limit time i.e. to
            datain.loc[6+cp1+cn1+c,'Longest Subsquence Length2']=datain.at[1+listp2[c]-scp2,'Time'] #lower limit time i. e. from
        for c in range (0,cn2):
            datain.loc[8+cp1+cn1+cp2+c,'Count2']=datain.at[listn2[c],'Time'] #upper limit time i.e. to
            datain.loc[8+cp1+cn1+cp2+c,'Longest Subsquence Length2']=datain.at[1+listn2[c]-scn2,'Time'] #lower limit time i. e. from
        for c in range (0,cp3):
            datain.loc[10+cp1+cn1+cp2+cn2+c,'Count2']=datain.at[listp3[c],'Time'] #upper limit time i.e. to
            datain.loc[10+cp1+cn1+cp2+cn2+c,'Longest Subsquence Length2']=datain.at[1+listp3[c]-scp3,'Time'] #lower limit time i. e. from
        for c in range (0,cn3):
            datain.loc[12+cp1+cn1+cp2+cn2+cp3+c,'Count2']=datain.at[listn3[c],'Time'] #upper limit time i.e. to
            datain.loc[12+cp1+cn1+cp2+cn2+cp3+c,'Longest Subsquence Length2']=datain.at[1+listn3[c]-scn3,'Time'] #lower limit time i. e. from
        for c in range (0,cp4):
            datain.loc[14+cp1+cn1+cp2+cn2+cp3+cn3+c,'Count2']=datain.at[listp4[c],'Time'] #upper limit time i.e. to
            datain.loc[14+cp1+cn1+cp2+cn2+cp3+cn3+c,'Longest Subsquence Length2']=datain.at[1+listp4[c]-scp4,'Time'] #lower limit time i. e. from
        for c in range (0,cn4):
            datain.loc[16+cp1+cn1+cp2+cn2+cp3+cn3+cp4+c,'Count2']=datain.at[listn4[c],'Time'] #upper limit time i.e. to
            datain.loc[16+cp1+cn1+cp2+cn2+cp3+cn3+cp4+c,'Longest Subsquence Length2']=datain.at[1+listn4[c]-scn4,'Time'] #lower limit time i. e. from
        #code written for desired work now converting dataframe to excel file
        try:  #this is try and except block
            datain.to_excel('output_octant_longest_subsequence_with_range.xlsx',index=False)# it makes a excel file with the name given in 'quote'
            print("Your desired output file is ready!!! Please Check!")
        except:
            print("the filename which you try to overwrite..Is it open or what? if it is open I cannot overwrite..please close")
                #index = false do not make make columns for index values as we have no requirement of it in this case    
    except FileNotFoundError: #this is except block of try and except.............3
        print("Hey...filename inputed by user is not found")
    
###Code
from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

octant_longest_subsequence_count_with_range() #calling function to get desired result