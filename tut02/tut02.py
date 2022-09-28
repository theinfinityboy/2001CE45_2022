import os
os.system("cls")
import pandas as pd
import numpy as np
import math
#importing libraries
os.chdir(r'C:\Users\pc\Documents\GitHub\2001CE45_2022\tut02')
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
def octant_transition_count(mod=5000):
###Code
    #readymadefunction having argument as mod value
    #complete code has been written in this(major portion)
    try:
        datain =  pd.read_excel('input_octant_transition_identify.xlsx') #reading input EXCEL file and storing in variable datain as data input
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
        datain['Octant']=np.nan #created a blank column named octant for which operation is to be done
        i=0 #initiating for loop variable
        while i<total_size: #loop is run for whole column size of input column file
            datain.loc[i,'Octant']=check_octant(datain.loc[i,'U-U_Avg'],datain.loc[i,'V-V_Avg'],datain.loc[i,'W-W_Avg'])
            #octant column is assigned octant value after chehking value of octant by calling function
            i=i+1 #updating loop

        datain['']=np.nan #new blank file and some processing according to the demand of output file has been done
        datain.loc[1,'']="User Input" #assigned a string at given index 1 acc. to output file
        datain['Octant Id']=np.nan 
        datain['+1']=np.nan
        datain['-1']=np.nan
        datain['+2']=np.nan
        datain['-2']=np.nan
        datain['+3']=np.nan
        datain['-3']=np.nan
        datain['+4']=np.nan
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
            datain.loc[i+2,'+1']=p1
            datain.loc[i+2,'-1']=n1
            datain.loc[i+2,'+2']=p2
            datain.loc[i+2,'-2']=n2
            datain.loc[i+2,'+3']=p3
            datain.loc[i+2,'-3']=n3
            datain.loc[i+2,'+4']=p4
            datain.loc[i+2,'-4']=n4
            i=i+1 
            #updating another parent loop having limit noi---no. of iterations reqd
            #after parent loop also broken 
            #we are assigning the values of overall count for each octant in the whole data using following comment

        datain.loc[0,'+1']=op1
        datain.loc[0,'-1']=on1
        datain.loc[0,'+2']=op2
        datain.loc[0,'-2']=on2
        datain.loc[0,'+3']=op3
        datain.loc[0,'-3']=on3
        datain.loc[0,'+4']=op4
        datain.loc[0,'-4']=on4
        #TILL HERE DONE........
        #verification for total mod count
        datain.loc[2+noi,'Octant Id']="Verified"#want a try and except block...
        sump1=0
        sumn1=0
        sump2=0
        sumn2=0
        sump3=0
        sumn3=0
        sump4=0
        sumn4=0
        i=0
        while i<noi:
            sump1= datain.loc[i+2,'+1']+sump1
            sumn1= datain.loc[i+2,'-1']+sumn1
            sump2= datain.loc[i+2,'+2']+sump2
            sumn2= datain.loc[i+2,'-2']+sumn2
            sump3= datain.loc[i+2,'+3']+sump3
            sumn3= datain.loc[i+2,'-3']+sumn3
            sump4= datain.loc[i+2,'+4']+sump4
            sumn4= datain.loc[i+2,'-4']+sumn4
            i=i+1
        datain.loc[2+noi,'+1']=sump1
        datain.loc[2+noi,'-1']=sumn1
        datain.loc[2+noi,'+2']=sump2
        datain.loc[2+noi,'-2']=sumn2
        datain.loc[2+noi,'+3']=sump3
        datain.loc[2+noi,'-3']=sumn3
        datain.loc[2+noi,'+4']=sump4
        datain.loc[2+noi,'-4']=sumn4
        #now counting for overall transition count
        datain.loc[5+noi,'Octant Id']="Overall Transition Count"
        datain.loc[7+noi,'Octant Id']="Count"
        datain.loc[8+noi,'Octant Id']='+1'
        datain.loc[9+noi,'Octant Id']='-1'
        datain.loc[10+noi,'Octant Id']='+2'
        datain.loc[11+noi,'Octant Id']='-2'
        datain.loc[12+noi,'Octant Id']='+3'
        datain.loc[13+noi,'Octant Id']='-3'
        datain.loc[14+noi,'Octant Id']='+4'
        datain.loc[15+noi,'Octant Id']='-4'
        datain.loc[6+noi,'+1']='To'
        datain.loc[8+noi,'']='From'
        datain.loc[7+noi,'+1']='+1'
        datain.loc[7+noi,'-1']='-1'
        datain.loc[7+noi,'+2']='+2'
        datain.loc[7+noi,'-2']='-2'
        datain.loc[7+noi,'+3']='+3'
        datain.loc[7+noi,'-3']='-3'
        datain.loc[7+noi,'+4']='+4'
        datain.loc[7+noi,'-4']='-4'
        #overall transition matrix made.....
        #now working for assigning value in it....
        #filling 0 in overall transition matrix
        for i in range(8+noi,16+noi):
            datain.loc[i,'+1']=0
            datain.loc[i,'-1']=0
            datain.loc[i,'+2']=0
            datain.loc[i,'-2']=0
            datain.loc[i,'+3']=0
            datain.loc[i,'-3']=0
            datain.loc[i,'+4']=0
            datain.loc[i,'-4']=0

        pos=19+noi #storing for position in a variable later to use in loop
        #for mod transition
        i=0
        while i<noi: 
            ll=i*mod
            if ((i+1)*mod)>=total_size:
                ul=total_size-1
            else:
                ul=(i+1)*mod-1
                #defined upper limit as ul and lower limit as ll
            #making mod transition matrix
            datain.loc[pos,'Octant Id']="Mod Transition Count"
            datain.loc[pos+1,'Octant Id']="{}-{}".format(ll,ul)
            datain.loc[pos+1,'+1']='To'
            datain.loc[pos+2,'Octant Id']="Count"
            datain.loc[pos+2,'+1']='+1'
            datain.loc[pos+2,'-1']='-1'
            datain.loc[pos+2,'+2']='+2'
            datain.loc[pos+2,'-2']='-2'
            datain.loc[pos+2,'+3']='+3'
            datain.loc[pos+2,'-3']='-3'
            datain.loc[pos+2,'+4']='+4'
            datain.loc[pos+2,'-4']='-4'
            datain.loc[pos+3,'']="From"
            datain.loc[pos+3,'Octant Id']="+1"
            datain.loc[pos+4,'Octant Id']="-1"
            datain.loc[pos+5,'Octant Id']="+2"
            datain.loc[pos+6,'Octant Id']="-2"
            datain.loc[pos+7,'Octant Id']="+3"
            datain.loc[pos+8,'Octant Id']="-3"
            datain.loc[pos+9,'Octant Id']="+4"
            datain.loc[pos+10,'Octant Id']="-4"
            #matrix prepared
            #assigning 0 to the each mod matrix
            for j in range(3+pos,11+pos):
                datain.loc[j,'+1']=0
                datain.loc[j,'-1']=0
                datain.loc[j,'+2']=0
                datain.loc[j,'-2']=0
                datain.loc[j,'+3']=0
                datain.loc[j,'-3']=0
                datain.loc[j,'+4']=0
                datain.loc[j,'-4']=0
            for z in range (ll,ul+1):
                
                if(datain.loc[z,'Octant']==1 and datain.loc[z+1,'Octant']==1):
                    datain.loc[pos+3,'+1']+=1 #for mod transition
                    datain.loc[8+noi,'+1']+=1 #for overall transition
                elif (datain.loc[z,'Octant']==1 and datain.loc[z+1,'Octant']==-1):
                    datain.loc[pos+3,'-1']+=1
                    datain.loc[8+noi,'-1']+=1
                elif (datain.loc[z,'Octant']==1 and datain.loc[z+1,'Octant']==2):
                    datain.loc[pos+3,'+2']+=1
                    datain.loc[8+noi,'+2']+=1
                elif (datain.loc[z,'Octant']==1 and datain.loc[z+1,'Octant']==-2):
                    datain.loc[pos+3,'-2']+=1
                    datain.loc[8+noi,'-2']+=1
                elif (datain.loc[z,'Octant']==1 and datain.loc[z+1,'Octant']==3):
                    datain.loc[pos+3,'+3']+=1
                    datain.loc[8+noi,'+3']+=1
                elif (datain.loc[z,'Octant']==1 and datain.loc[z+1,'Octant']==-3):
                    datain.loc[pos+3,'-3']+=1
                    datain.loc[8+noi,'-3']+=1
                elif (datain.loc[z,'Octant']==1 and datain.loc[z+1,'Octant']==4):
                    datain.loc[pos+3,'+4']+=1
                    datain.loc[8+noi,'+4']+=1
                elif (datain.loc[z,'Octant']==1 and datain.loc[z+1,'Octant']==-4):
                    datain.loc[pos+3,'-4']+=1
                    datain.loc[8+noi,'-4']+=1
                #updated row corresponding to from +1 to any transition (mod or overall) 
                #now for -1
                if(datain.loc[z,'Octant']==-1 and datain.loc[z+1,'Octant']==1):
                    datain.loc[pos+4,'+1']+=1 #for mod transition
                    datain.loc[9+noi,'+1']+=1 #for overall transition
                elif (datain.loc[z,'Octant']==-1 and datain.loc[z+1,'Octant']==-1):
                    datain.loc[pos+4,'-1']+=1
                    datain.loc[9+noi,'-1']+=1
                elif (datain.loc[z,'Octant']==-1 and datain.loc[z+1,'Octant']==2):
                    datain.loc[pos+4,'+2']+=1
                    datain.loc[9+noi,'+2']+=1
                elif (datain.loc[z,'Octant']==-1 and datain.loc[z+1,'Octant']==-2):
                    datain.loc[pos+4,'-2']+=1
                    datain.loc[9+noi,'-2']+=1
                elif (datain.loc[z,'Octant']==-1 and datain.loc[z+1,'Octant']==3):
                    datain.loc[pos+4,'+3']+=1
                    datain.loc[9+noi,'+3']+=1
                elif (datain.loc[z,'Octant']==-1 and datain.loc[z+1,'Octant']==-3):
                    datain.loc[pos+4,'-3']+=1
                    datain.loc[9+noi,'-3']+=1
                elif (datain.loc[z,'Octant']==-1 and datain.loc[z+1,'Octant']==4):
                    datain.loc[pos+4,'+4']+=1
                    datain.loc[9+noi,'+4']+=1
                elif (datain.loc[z,'Octant']==-1 and datain.loc[z+1,'Octant']==-4):
                    datain.loc[pos+4,'-4']+=1
                    datain.loc[9+noi,'-4']+=1
                #updated row corresponding to from -1 to any transition (mod or overall) 
                #now for +2
                if(datain.loc[z,'Octant']==2 and datain.loc[z+1,'Octant']==1):
                    datain.loc[pos+5,'+1']+=1 #for mod transition
                    datain.loc[10+noi,'+1']+=1 #for overall transition
                elif (datain.loc[z,'Octant']==2 and datain.loc[z+1,'Octant']==-1):
                    datain.loc[pos+5,'-1']+=1
                    datain.loc[10+noi,'-1']+=1
                elif (datain.loc[z,'Octant']==2 and datain.loc[z+1,'Octant']==2):
                    datain.loc[pos+5,'+2']+=1
                    datain.loc[10+noi,'+2']+=1
                elif (datain.loc[z,'Octant']==2 and datain.loc[z+1,'Octant']==-2):
                    datain.loc[pos+5,'-2']+=1
                    datain.loc[10+noi,'-2']+=1
                elif (datain.loc[z,'Octant']==2 and datain.loc[z+1,'Octant']==3):
                    datain.loc[pos+5,'+3']+=1
                    datain.loc[10+noi,'+3']+=1
                elif (datain.loc[z,'Octant']==2 and datain.loc[z+1,'Octant']==-3):
                    datain.loc[pos+5,'-3']+=1
                    datain.loc[10+noi,'-3']+=1
                elif (datain.loc[z,'Octant']==2 and datain.loc[z+1,'Octant']==4):
                    datain.loc[pos+5,'+4']+=1
                    datain.loc[10+noi,'+4']+=1
                elif (datain.loc[z,'Octant']==2 and datain.loc[z+1,'Octant']==-4):
                    datain.loc[pos+5,'-4']+=1
                    datain.loc[10+noi,'-4']+=1
                #updated row corresponding to from +2 to any transition (mod or overall)  

                #now for -2
                if(datain.loc[z,'Octant']==-2 and datain.loc[z+1,'Octant']==1):
                    datain.loc[pos+6,'+1']+=1 #for mod transition
                    datain.loc[11+noi,'+1']+=1 #for overall transition
                elif (datain.loc[z,'Octant']==-2 and datain.loc[z+1,'Octant']==-1):
                    datain.loc[pos+6,'-1']+=1
                    datain.loc[11+noi,'-1']+=1
                elif (datain.loc[z,'Octant']==-2 and datain.loc[z+1,'Octant']==2):
                    datain.loc[pos+6,'+2']+=1
                    datain.loc[11+noi,'+2']+=1
                elif (datain.loc[z,'Octant']==-2 and datain.loc[z+1,'Octant']==-2):
                    datain.loc[pos+6,'-2']+=1
                    datain.loc[11+noi,'-2']+=1
                elif (datain.loc[z,'Octant']==-2 and datain.loc[z+1,'Octant']==3):
                    datain.loc[pos+6,'+3']+=1
                    datain.loc[11+noi,'+3']+=1
                elif (datain.loc[z,'Octant']==-2 and datain.loc[z+1,'Octant']==-3):
                    datain.loc[pos+6,'-3']+=1
                    datain.loc[11+noi,'-3']+=1
                elif (datain.loc[z,'Octant']==-2 and datain.loc[z+1,'Octant']==4):
                    datain.loc[pos+6,'+4']+=1
                    datain.loc[11+noi,'+4']+=1
                elif (datain.loc[z,'Octant']==-2 and datain.loc[z+1,'Octant']==-4):
                    datain.loc[pos+6,'-4']+=1
                    datain.loc[11+noi,'-4']+=1
                #updated row corresponding to from -2 to any transition (mod or overall)

                #now for +3
                if(datain.loc[z,'Octant']==3 and datain.loc[z+1,'Octant']==1):
                    datain.loc[pos+7,'+1']+=1 #for mod transition
                    datain.loc[12+noi,'+1']+=1 #for overall transition
                elif (datain.loc[z,'Octant']==3 and datain.loc[z+1,'Octant']==-1):
                    datain.loc[pos+7,'-1']+=1
                    datain.loc[12+noi,'-1']+=1
                elif (datain.loc[z,'Octant']==3 and datain.loc[z+1,'Octant']==2):
                    datain.loc[pos+7,'+2']+=1
                    datain.loc[12+noi,'+2']+=1
                elif (datain.loc[z,'Octant']==3 and datain.loc[z+1,'Octant']==-2):
                    datain.loc[pos+7,'-2']+=1
                    datain.loc[12+noi,'-2']+=1
                elif (datain.loc[z,'Octant']==3 and datain.loc[z+1,'Octant']==3):
                    datain.loc[pos+7,'+3']+=1
                    datain.loc[12+noi,'+3']+=1
                elif (datain.loc[z,'Octant']==3 and datain.loc[z+1,'Octant']==-3):
                    datain.loc[pos+7,'-3']+=1
                    datain.loc[12+noi,'-3']+=1
                elif (datain.loc[z,'Octant']==3 and datain.loc[z+1,'Octant']==4):
                    datain.loc[pos+7,'+4']+=1
                    datain.loc[12+noi,'+4']+=1
                elif (datain.loc[z,'Octant']==3 and datain.loc[z+1,'Octant']==-4):
                    datain.loc[pos+7,'-4']+=1
                    datain.loc[12+noi,'-4']+=1
                #updated row corresponding to from +3 to any transition (mod or overall) 

                #now for -3
                if(datain.loc[z,'Octant']==-3 and datain.loc[z+1,'Octant']==1):
                    datain.loc[pos+8,'+1']+=1 #for mod transition
                    datain.loc[13+noi,'+1']+=1 #for overall transition
                elif (datain.loc[z,'Octant']==-3 and datain.loc[z+1,'Octant']==-1):
                    datain.loc[pos+8,'-1']+=1
                    datain.loc[13+noi,'-1']+=1
                elif (datain.loc[z,'Octant']==-3 and datain.loc[z+1,'Octant']==2):
                    datain.loc[pos+8,'+2']+=1
                    datain.loc[13+noi,'+2']+=1
                elif (datain.loc[z,'Octant']==-3 and datain.loc[z+1,'Octant']==-2):
                    datain.loc[pos+8,'-2']+=1
                    datain.loc[13+noi,'-2']+=1
                elif (datain.loc[z,'Octant']==-3 and datain.loc[z+1,'Octant']==3):
                    datain.loc[pos+8,'+3']+=1
                    datain.loc[13+noi,'+3']+=1
                elif (datain.loc[z,'Octant']==-3 and datain.loc[z+1,'Octant']==-3):
                    datain.loc[pos+8,'-3']+=1
                    datain.loc[13+noi,'-3']+=1
                elif (datain.loc[z,'Octant']==-3 and datain.loc[z+1,'Octant']==4):
                    datain.loc[pos+8,'+4']+=1
                    datain.loc[13+noi,'+4']+=1
                elif (datain.loc[z,'Octant']==-3 and datain.loc[z+1,'Octant']==-4):
                    datain.loc[pos+8,'-4']+=1
                    datain.loc[13+noi,'-4']+=1
                #updated row corresponding to from -3 to any transition (mod or overall)     
                #now for +4
                if(datain.loc[z,'Octant']==4 and datain.loc[z+1,'Octant']==1):
                    datain.loc[pos+9,'+1']+=1 #for mod transition
                    datain.loc[14+noi,'+1']+=1 #for overall transition
                elif (datain.loc[z,'Octant']==4 and datain.loc[z+1,'Octant']==-1):
                    datain.loc[pos+9,'-1']+=1
                    datain.loc[14+noi,'-1']+=1
                elif (datain.loc[z,'Octant']==4 and datain.loc[z+1,'Octant']==2):
                    datain.loc[pos+9,'+2']+=1
                    datain.loc[14+noi,'+2']+=1
                elif (datain.loc[z,'Octant']==4 and datain.loc[z+1,'Octant']==-2):
                    datain.loc[pos+9,'-2']+=1
                    datain.loc[14+noi,'-2']+=1
                elif (datain.loc[z,'Octant']==4 and datain.loc[z+1,'Octant']==3):
                    datain.loc[pos+9,'+3']+=1
                    datain.loc[14+noi,'+3']+=1
                elif (datain.loc[z,'Octant']==4 and datain.loc[z+1,'Octant']==-3):
                    datain.loc[pos+9,'-3']+=1
                    datain.loc[14+noi,'-3']+=1
                elif (datain.loc[z,'Octant']==4 and datain.loc[z+1,'Octant']==4):
                    datain.loc[pos+9,'+4']+=1
                    datain.loc[14+noi,'+4']+=1
                elif (datain.loc[z,'Octant']==4 and datain.loc[z+1,'Octant']==-4):
                    datain.loc[pos+9,'-4']+=1
                    datain.loc[14+noi,'-4']+=1
                #updated row corresponding to from +4 to any transition (mod or overall)  
                #now for -4
                if(datain.loc[z,'Octant']==-4 and datain.loc[z+1,'Octant']==1):
                    datain.loc[pos+10,'+1']+=1 #for mod transition
                    datain.loc[15+noi,'+1']+=1 #for overall transition
                elif (datain.loc[z,'Octant']==-4 and datain.loc[z+1,'Octant']==-1):
                    datain.loc[pos+10,'-1']+=1
                    datain.loc[15+noi,'-1']+=1
                elif (datain.loc[z,'Octant']==-4 and datain.loc[z+1,'Octant']==2):
                    datain.loc[pos+10,'+2']+=1
                    datain.loc[15+noi,'+2']+=1
                elif (datain.loc[z,'Octant']==-4 and datain.loc[z+1,'Octant']==-2):
                    datain.loc[pos+10,'-2']+=1
                    datain.loc[15+noi,'-2']+=1
                elif (datain.loc[z,'Octant']==-4 and datain.loc[z+1,'Octant']==3):
                    datain.loc[pos+10,'+3']+=1
                    datain.loc[15+noi,'+3']+=1
                elif (datain.loc[z,'Octant']==-4 and datain.loc[z+1,'Octant']==-3):
                    datain.loc[pos+10,'-3']+=1
                    datain.loc[15+noi,'-3']+=1
                elif (datain.loc[z,'Octant']==-4 and datain.loc[z+1,'Octant']==4):
                    datain.loc[pos+10,'+4']+=1
                    datain.loc[15+noi,'+4']+=1
                elif (datain.loc[z,'Octant']==-4 and datain.loc[z+1,'Octant']==-4):
                    datain.loc[pos+10,'-4']+=1
                    datain.loc[15+noi,'-4']+=1
                    #updated row corresponding to from -4 to any transition (mod or overall)  
                if(z==total_size-2):
                    break   
                    #here we used break statement because we need to traverse to total no. of rows minus 1 because indexing in python is from zero
                    #and due to this last element of row will be at index total size -1
                    #and we need to traverse to 2nd last row only so breaking loop at 2nd last element
                
            pos=pos+13 #updating position for next iteration
            i=i+1

        
        #matrix made now 
        #all work done now we have desired dataframe which we need to convert in EXCEL file using the command below
        datain.to_excel('output_octant_transition_identify.xlsx',index=False)# it makes a csv file with the name given in 'quote'
        #index = false do not make make columns for index values as we have no requirement of it in this case
        print("Your desired output file is ready!!! Please Check!")
    except FileNotFoundError:
        print("Hey...file inputed by user is not found")

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000    #this is user input user can change it
octant_transition_count(mod)