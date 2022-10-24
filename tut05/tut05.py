#Help https://youtu.be/N6PBd4XdnEw
import os
os.system("cls")
import pandas as pd
import numpy as np
import math
#importing libraries
os.chdir(r'C:\Users\pc\Documents\GitHub\2001CE45_2022\tut05')
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
def octant_range_names(mod=5000):
    #readymadefunction having argument as mod value
    #complete code has been written in this(major portion)
    try:
        datain =  pd.read_excel('octant_input.xlsx') #reading input excel file and storing in variable datain as data input
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
        datain['U-U_Avg']=datain['U']-U_Avg
        datain['V-V_Avg']=datain['V']-V_Avg
        datain['W-W_Avg']=datain['W']-W_Avg
        #three more columns have been made and assigned value as V-Vavg.....corresponding name and corresponding columns
        datain['Octant']=np.nan 
        #created a blank column named octant for which operation is to be done
        i=0 #initiating for loop variable
        while i<total_size: #loop is run for whole column size of input column file
            datain.loc[i,'Octant']=check_octant(datain.loc[i,'U-U_Avg'],datain.loc[i,'V-V_Avg'],datain.loc[i,'W-W_Avg'])
            #octant column is assigned octant value after chehking value of octant by calling function
            i=i+1 #updating loop

        datain['']=np.nan #new blank file and some processing according to the demand of output file has been done
        datain.loc[1,'']="User Input" #assigned a string at given index 1 acc. to output file
        datain['Octant Id']=np.nan 
        datain['1']=np.nan
        datain['-1']=np.nan
        datain['2']=np.nan
        datain['-2']=np.nan
        datain['3']=np.nan
        datain['-3']=np.nan
        datain['4']=np.nan
        datain['-4']=np.nan

        #new columns has been made for further proceedings
        datain.loc[0,'Octant Id']="Overall Count" #filling the columns according to output file demand
        datain.loc[1,'Octant Id']="mod {}".format(mod)
        #again filling the column but this time adding parameters in it on which the next processing depends
        noi = math.ceil(total_size/mod) #here ceil value provides the upper bound of the floating no...e.g..7.4 have ceil value 8
        #this will reflect no. of iterations to be performed or no. of sections in which our input file will be divided to check the count 
        i=0 #initiated for iteration
        op1=0
        on1=0
        op2=0
        on2=0
        op3=0
        on3=0
        op4=0
        on4=0
        #initiated to count overall count of each octant op1-overall positive 1,on1-overall negative 1
        while i<noi: #loop conditions
            if(i+1)*mod>total_size: 
                u=total_size-1 
            else:             #u is the condition or limit for upper boundary of the mod ranged values
                u=(i+1)*mod-1
            l=i*mod          #similarly l is the lower boundary
            datain.loc[i+2,'Octant Id']="{}-{}".format(l,u) #filling mod ranged section as its demand of sections should not count more than mod value count columns
            j=0 #initiated for loop
            p1=0
            n1=0
            p2=0
            n2=0
            p3=0
            n3=0
            p4=0
            n4=0
            #these values initiated for filling frequency of occurence of octant in each mod range 
            #p1--positive 1.......n1--negative 1

            #this is loop is being run to count the each octant values in each column range max of mod and and calculate total occurence of each occurence in the column range

            while j<mod: #loop condition
                
                pos =(i*mod)+j #variable to get the column no. where exactly we are counting the octant value
                if pos>=total_size:
                    break #conditions fulfilling criteria of loop
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
                        p3=p3+1
                    elif datain.loc[pos,'Octant']==-3:
                        n3=n3+1
                    elif datain.loc[pos,'Octant']==4:
                        p4=p4+1
                    elif datain.loc[pos,'Octant']==-4:
                        n4=n4+1 
                        #updating each variables counting octants and storing in the range of mod valued difference class
                j=j+1 #loop updating

            op1=op1+p1
            on1=on1+n1
            op2=op2+p2
            on2=on2+n2
            op3=op3+p3
            on3=on3+n3
            op4=op4+p4
            on4=on4+n4
            #updating overall count of each octant value in our input datawhere it lies

            #//when loop is broken for mod range value the value is stored in the desired location using following command
            datain.loc[i+2,'1']=p1
            datain.loc[i+2,'-1']=n1
            datain.loc[i+2,'2']=p2
            datain.loc[i+2,'-2']=n2
            datain.loc[i+2,'3']=p3
            datain.loc[i+2,'-3']=n3
            datain.loc[i+2,'4']=p4
            datain.loc[i+2,'-4']=n4
            i=i+1 
            #updating another parent loop having limit noi---no. of iterations reqd
            #after parent loop also broken 
            #we are assigning the values of overall count for each octant in the whole data using following comment

        datain.loc[0,'1']=op1
        datain.loc[0,'-1']=on1
        datain.loc[0,'2']=op2
        datain.loc[0,'-2']=on2
        datain.loc[0,'3']=op3
        datain.loc[0,'-3']=on3
        datain.loc[0,'4']=op4
        datain.loc[0,'-4']=on4
######################################################################################################################################
        #now finding rank based on octant appearance
        datain['Rank 1(oct 1)']=np.nan
        datain['Rank 2(oct -1)']=np.nan
        datain['Rank 3(oct 2)']=np.nan
        datain['Rank 4(oct -2)']=np.nan
        datain['Rank 5(oct 3)']=np.nan
        datain['Rank 6(oct -3)']=np.nan
        datain['Rank 7(oct 4)']=np.nan
        datain['Rank 8(oct -4)']=np.nan
        datain['Rank 1 Octant Id']=np.nan
        datain['Rank 1 Octant Name']=np.nan
        #created column for writing rank values
        datain.loc[noi+5,'1']="Octant Id"
        datain.loc[noi+5,'-1']="Octant Name"
        datain.loc[noi+5,'2']="Count of Rank 1 Mod values"
        ##created required matrix 
        #now, writing program for finding rank of matrix....and filling matrix
        octant_name_id_mapping = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}
        #this dictionary has been made to name the corresponding octant
        datain.loc[noi+6,'1']="1"
        datain.loc[noi+7,'1']="-1"
        datain.loc[noi+8,'1']="2"
        datain.loc[noi+9,'1']="-2"
        datain.loc[noi+10,'1']="3"
        datain.loc[noi+11,'1']="-3"
        datain.loc[noi+12,'1']="4"
        datain.loc[noi+13,'1']="-4"
        datain.loc[noi+6,'-1']=octant_name_id_mapping["1"]
        datain.loc[noi+7,'-1']=octant_name_id_mapping["-1"]
        datain.loc[noi+8,'-1']=octant_name_id_mapping["2"]
        datain.loc[noi+9,'-1']=octant_name_id_mapping["-2"]
        datain.loc[noi+10,'-1']=octant_name_id_mapping["3"]
        datain.loc[noi+11,'-1']=octant_name_id_mapping["-3"]
        datain.loc[noi+12,'-1']=octant_name_id_mapping["4"]
        datain.loc[noi+13,'-1']=octant_name_id_mapping["-4"]
        #filled matrix required as according to tutorial corresponding to their requirement #no logic used used till now
        i=0 #we will do iteration for the all rank count and write the count for one iteration...
        r1cp1=r1cn1=r1cp2=r1cn2=r1cp3=r1cn3=r1cp4=r1cn4=0 
        #variable initiated for rank 1 count p(positive)/n(negative) octant id we will use it later for rank 1 appearance in the mod values of diff. octant id
        while (i<noi+2):
            if(i==1):
                i=i+1 #this has been done because we no values at the 1 st row(index basis)i.e. no values for octant id in the 2nd row
            rank_dict = {datain.loc[i,'1'] :"1",datain.loc[i,'-1'] :"-1",datain.loc[i,'2'] :"2",datain.loc[i,'-2'] :"-2",datain.loc[i,'3'] :"3",datain.loc[i,'-3'] :"-3",datain.loc[i,'4'] :"4",datain.loc[i,'-4'] :"-4"}
            #initiated dictionary of values at corresponding row iteration at different columns with their column name as value
            rank_list =[datain.loc[i,'1'],datain.loc[i,'-1'],datain.loc[i,'2'],datain.loc[i,'-2'],datain.loc[i,'3'],datain.loc[i,'-3'],datain.loc[i,'4'],datain.loc[i,'-4'] ]
            #created list and sorted in next step to get the rank on the basis of indexes easily....
            rank_list.sort() 
            for j in range(8):
                lok=rank_dict[rank_list[j]] #made variable to use it frequently with ease
                if (lok=="1"):
                    datain.loc[i,'Rank 1(oct 1)']=8-j
                if (lok=="-1"):
                    datain.loc[i,'Rank 2(oct -1)']=8-j
                if (lok=="2"):
                    datain.loc[i,'Rank 3(oct 2)']=8-j
                if (lok=="-2"):
                    datain.loc[i,'Rank 4(oct -2)']=8-j
                if (lok=="3"):
                    datain.loc[i,'Rank 5(oct 3)']=8-j
                if (lok=="-3"):
                    datain.loc[i,'Rank 6(oct -3)']=8-j
                if (lok=="4"):
                    datain.loc[i,'Rank 7(oct 4)']=8-j
                if (lok=="-4"):
                    datain.loc[i,'Rank 8(oct -4)']=8-j
                    #assigning rank values of each octant in each mod value range as well as overall data in its corresponding column
            datain.loc[i,'Rank 1 Octant Id']=rank_dict[rank_list[7]]
            #since out list are sorted in ascending order so we are traversing from back side to get the max value in the list to assign it as rank 1
            datain.loc[i,'Rank 1 Octant Name']=octant_name_id_mapping[datain.loc[i,'Rank 1 Octant Id']]
            ##now we will be counting rant one appearance of each octant...
            if(i>1):
                #this we have done beacause we have to count the rank one value for each mod duration only
                if(datain.loc[i,'Rank 1 Octant Id']=="1"):
                    r1cp1+=1
                if(datain.loc[i,'Rank 1 Octant Id']=="-1"):
                    r1cn1+=1
                if(datain.loc[i,'Rank 1 Octant Id']=="2"):
                    r1cp2+=1
                if(datain.loc[i,'Rank 1 Octant Id']=="-2"):
                    r1cn2+=1
                if(datain.loc[i,'Rank 1 Octant Id']=="3"):
                    r1cp3+=1
                if(datain.loc[i,'Rank 1 Octant Id']=="-3"):
                    r1cn3+=1
                if(datain.loc[i,'Rank 1 Octant Id']=="4"):
                    r1cp4+=1
                if(datain.loc[i,'Rank 1 Octant Id']=="-4"):
                    r1cn4+=1
                    #all values will be updated at end of the iteration
            i=i+1
        datain.loc[noi+6,'2']=r1cp1
        datain.loc[noi+7,'2']=r1cn1
        datain.loc[noi+8,'2']=r1cp2
        datain.loc[noi+9,'2']=r1cn2
        datain.loc[noi+10,'2']=r1cp3
        datain.loc[noi+11,'2']=r1cn3
        datain.loc[noi+12,'2']=r1cp4
        datain.loc[noi+13,'2']=r1cn4
        #assigning value in the required matrix with the help of variable initiated earlier
        
        
        #code written for desired work now converting dataframe to excel file
        try:  #this is try and except block
            datain.to_excel('octant_output_ranking_excel.xlsx',index=False)# it makes a excel file with the name given in 'quote'
            print("Your desired output file is ready!!! Please Check!")
        except:
            print("the filename which you try to overwrite..Is it open or what? if it is open I cannot overwrite..please close")
                #index = false do not make make columns for index values as we have no requirement of it in this case    
    except FileNotFoundError:
        print("Hey...file inputed by user is not found")
###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


mod=5000 
#user data
octant_range_names(mod)
#calling required function

