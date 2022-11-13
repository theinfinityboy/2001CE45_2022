# importing required libraries
import os
from urllib import response
import pandas as pd
from datetime import date
from datetimerange import DateTimeRange
os.chdir(r'C:\Users\pc\Documents\GitHub\2001CE45_2022\tut06')
path = os.path.join(r'C:\Users\pc\Documents\GitHub\2001CE45_2022\tut06\output') 
if os.path.exists(path)==False:
    os.mkdir(path)

from datetime import datetime
start_time = datetime.now()

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

def attendance_report():
    # myreader1 and myreader2 read and store the input_attendance.csv and input_registered_students.csv files respectively.
    myreader1=pd.read_csv('input_attendance.csv')
    myreader2=pd.read_csv('input_registered_students.csv')
    os.chdir(r'C:\Users\pc\Documents\GitHub\2001CE45_2022\tut06\output') 
    #changed directory to save output file in it
    size=myreader1['Timestamp'].size 
    #this would be no. of rows in input attendance file
    mylist=[] #a blank list has been made we will later store each cell of Timestamp
    myset=set() #empty set has been made to catch the duplicate attendance

    for i in range(size): 
    #running for loop to count total no. of days on which lecture was taken
        mylist.append((myreader1['Timestamp'][i])) 
        a=str(mylist[i]) 
        #typecasting ith element of mylist and storing in a
        if a[0]==str(0): 
        #uusing if else struct. to get the day from the date that has baan obtained timestamp
            a1=a[1] #applying this condition for the date <10,i.e. 01,02....09
        else:
            a1=a[0:2] #otherwise to implement the else
        if a[3]==str(0): 
            a2=a[4]
             #similarly if else to get month from the date(from timestamp)
            #similar condition of <10..
        else:
            a2=a[3:5]

        time=date(2022,int(a2),int(a1)) #from lib datetime using the dateclass
        if time.strftime('%A')== 'Monday' or time.strftime('%A')== 'Thursday':
            #condition checking mondays and thursdays if attendance were marked
            if int(a2)<10 and int(a1)<10:
                myset.add('0'+str(a1)+'/'+'0'+str(a2)+'/'+str(2022)) 
                #if true date added to the set
            elif int(a2)<10 and int(a1)>=10:
                myset.add(str(a1)+'/'+'0'+str(a2)+'/'+str(2022)) 
            elif int(a2)>10 and int(a1)<10:
                myset.add('0'+str(a1)+'/'+str(a2)+'/'+str(2022)) 
            elif int(a2)>10 and int(a1)>10:
                myset.add(str(a1)+'/'+str(a2)+'/'+str(2022)) 
    total=len(myset)  #here we counted total no. pf lectures
    myset_list=list(myset) #conversion of set in the list
    myset_list.sort(key=lambda date: datetime.strptime(date, "%d/%m/%Y")) 
    #based on the date sorting of list has been done
    size_class=myreader2['Roll No'].size 
    #size of class from the dataframe obtained by file input_registered_students.csv
    df2=pd.DataFrame()  
    #creating dataframe for consolidated attendance report
    for i in range(size_class):
        #creating dataframe for every stud in the loop
        df=pd.DataFrame() 
        a1=''
        real_total=0 #stores real att.
        duplicate=0 #stores duplicate attn.

        df['Date']='' #creating first column date
        df.loc[0,'Roll']=myreader2['Roll No'][i] 
        roll=myreader2['Roll No'][i] 
        df.loc[0,'Name']=myreader2['Name'][i] 
        #wrote name and roll to dataframe df

        df2.loc[i,'Roll']=roll  
        df2.loc[i,'Name']=df.loc[0,'Name'] 
        #adding roll no. and name column to df2
        for rjb in range(1,total+1): #setting some default values in df and df2
            df.loc[rjb,'Date']=myset_list[rjb-1] #writing date in df
            df.loc[rjb,'Total Attendance Count']=0
            df.loc[rjb,'Real']=0 
            df.loc[rjb,'Duplicate']=0
            df.loc[rjb,'Invalid']=0
            df.loc[rjb,'Absent']=1
            df2.loc[i,myset_list[rjb-1]]='A'
            #date column has been created and in df2 and assingned default A as absent...later we will change in case of present
            
        
        for j in range(size): 
            real=0 
            invalid=0 
            #STORING REAL AND INVALID ATTENDANCE
            if str(myreader2['Roll No'][i]) in str(myreader1['Attendance'][j]): 
                # we will proceed in case of roll no. present in the column
                a=str(mylist[j]) #accecing alement of my list
                date_1,time_1=verify(myreader1['Timestamp'][j]) #verifying from the func..
                if date_1==1: #found the day as monday/thursday
                    if time_1==1: #found time within 2-3 pm
                        real+=1 
                        real_total+=1 
                        #increament in the real attd.
                        if a[0:14] in a1: 
                            # if a[0:14] that is specific date and time, already in a1 which is the collection of all such strings 'a'.
                            duplicate+=1
                        else:
                            duplicate=0 
                    else:  # if not within 2-3 PM, invalid becomes 1.
                        invalid+=1
                    
                    
                    for rjb2 in range(1,total+1):
                        x = myset_list[rjb2-1]
                        datetime_str = datetime.strptime(x, '%d/%m/%Y')
                        datetime_str = datetime.strftime(datetime_str, '%d-%m-%Y')
                        if a[0:10]==datetime_str:
                            
                            df.loc[rjb2,'Total Attendance Count']=real+duplicate #total lecture taken to df
                            df.loc[rjb2,'Real']=int(real) 
                            df.loc[rjb2,'Duplicate']=int(duplicate) 
                            df.loc[rjb2,'Invalid']=int(invalid) 
                            if real>0:
                                df.loc[rjb2,'Absent']=0
                            break

                a1+=a    #adding a to a1(a1 cross checks with all timestamp that would appear in future iterations and ppoint out duplicate)
                if real==1: 
                    df2.iloc[i,rjb2]='P'
                    # if real ==1 and THEN P will replace A WHICH WAS FILLED BY DEFAULT EARLIER IN THIS CODE

        df2.loc[i,'Actual Lecture Taken']=total 
        df2.loc[i,'Total Real']=real_total
        df2.loc[i,'% Attendance']=round(real_total/total,4)*100
        #UPDATED THE MATRIX FOR ROLL FILE
        try:
            df.to_excel(f'{roll}.xlsx',index=False)
        except:
            print("check if{}.csv is open or what?, there was error in making/overwrite this file. if open pls close the file and re run the programme".format(roll))
        #FILE ,MADE FOR EACH ROLL NO.
    
    return df2  #consolidated dataframe of all individual dataframes.
    
def verify(time): #FUNCTION TO CHECK TIMESTAMP VALIDITY

    if time[0]==str(0): 
        a1=time[1] #same as done earlier...conditions to store a1 and a2
    else:
        a1=time[0:2]

    if time[3]==str(0):
        a2=time[4]
    else:
        a2=time[3:5]

    time1=date(2022,int(a2),int(a1)) #input format---constructor class date
    time2=f'{time1}T{time[11:]}' #time range checking--combined format
    time_range = DateTimeRange(f'{time1}T14:00:00', f'{time1}T15:00:00') 
    #2-3 pm time interval checking
    #date checking
    if time1.strftime('%A')== 'Monday' or time1.strftime('%A')== 'Thursday':
        if time2 in time_range: 
            return 1,1
        else:
            return 1,0
    else:
        return 0,0

# libraries needed to send a mail
import smtplib
from pathlib import Path
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

def send_mail(send_from, send_to, subject, message, path,password,
            server='smtp.gmail.com', port=465):

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(message))
    part = MIMEBase('application', "octet-stream")

    with open(path, 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename={}'.format(Path(path).name))
    msg.attach(part)

    context=ssl.create_default_context()
    with smtplib.SMTP_SSL(server,port,context=context) as smtp:
        smtp.login(send_from, password)
        smtp.sendmail(send_from, send_to, msg.as_string())

    print("Please check your mail. If not in inbox, please check spam!")

 
try:
    df2=attendance_report() 
    try:
        df2.to_excel('attendance_report_consolidated.xlsx',index=False) 
        print('The files have been created.')
    except:
        print('check if attendance_report_consolidated.xlsx is already open or what? if open please close.. ')
    
    response=int(input("Do you want to email this file using gmail id? For 'yes' enter 1, for 'no' enter 0:")) # asking if user wants to send on given email id
    try:
        if response==1:
            send_mail('enteryourgmail@gmail.com','cs3842022@gmail.com','Please find attachment.','attendance_report_consolidated.csv is attached',
            'attendance_report_consolidated.csv','ChangeMe PASSWORD') 
    except:
        print('Connect to the internet and retry.')
        print('Error in sending an email! These could be the possible reasons.\nConfigure your email account to allow sending emails via third-party apps (Python in this case). For gmail account, use the following steps:\n')
        print('\ta. Go to myaccount.google.com and sign into your gmail account if required.\n\tb.Under "Security" turn on 2 step verification using your phone number. \n\tc. Go to myaccout.google.com/apppasswords and you will be asked to sign in\n\td. Under "Select app" choose "Other", and type Python in the box.\n\te.A 16 digit password appears on the screen which can be used to login here when calling the function send_mail().')
        print('Use the correct server and correct port. For gmail IDs, the correct server and port has been given.')
        print('The correct file path was not specified.')
    
        
except:
    print('Error occured in reading file input_attendance.csv. Please change the date-format of the timestamps to dd/mm/yyyy or use a fresh input file.')

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
