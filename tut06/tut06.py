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

        if a[0]==str(0): 
            a1=a[1] 
        else:
            a1=a[0:2]
        if a[3]==str(0): 
            a2=a[4] 
        else:
            a2=a[3:5]

        time=date(2022,int(a2),int(a1)) 
        if time.strftime('%A')== 'Monday' or time.strftime('%A')== 'Thursday':
            if int(a2)<10 and int(a1)<10:
                myset.add('0'+str(a1)+'/'+'0'+str(a2)+'/'+str(2022)) 
            elif int(a2)<10 and int(a1)>=10:
                myset.add(str(a1)+'/'+'0'+str(a2)+'/'+str(2022)) 
            elif int(a2)>10 and int(a1)<10:
                myset.add('0'+str(a1)+'/'+str(a2)+'/'+str(2022)) 
            elif int(a2)>10 and int(a1)>10:
                myset.add(str(a1)+'/'+str(a2)+'/'+str(2022)) 
    total=len(myset)  
    myset_list=list(myset) 
    myset_list.sort(key=lambda date: datetime.strptime(date, "%d/%m/%Y")) 

    size_class=myreader2['Roll No'].size 
    df2=pd.DataFrame()  

    for i in range(size_class):
        df=pd.DataFrame() 
        a1=''
        real_total=0 
        duplicate=0 

        df['Date']=''
        df.loc[0,'Roll']=myreader2['Roll No'][i] 
        roll=myreader2['Roll No'][i] 
        df.loc[0,'Name']=myreader2['Name'][i] 

        df2.loc[i,'Roll']=roll 
        df2.loc[i,'Name']=df.loc[0,'Name'] 
        for row1 in range(1,total+1): 
            df.loc[row1,'Date']=myset_list[row1-1] 
            df.loc[row1,'Total Attendance Count']=0
            df.loc[row1,'Real']=0 
            df.loc[row1,'Duplicate']=0
            df.loc[row1,'Invalid']=0
            df.loc[row1,'Absent']=0
            df2.loc[i,myset_list[row1-1]]='A'

        for j in range(size):
            real=0 
            invalid=0 

            if str(myreader2['Roll No'][i]) in str(myreader1['Attendance'][j]): 
                a=str(mylist[j]) 
                date_1,time_1=verify(myreader1['Timestamp'][j]) 
                if date_1==1: 
                    if time_1==1: 
                        real+=1 
                        real_total+=1 
                        if a[0:14] in a1: 
                            duplicate+=1
                        else:
                            duplicate=0 
                    else:
                        invalid+=1

                    for row2 in range(1,total+1):
                        if a[0:10]== myset_list[row2-1]:
                            df.loc[row2,'Total Attendance Count']=real+duplicate 
                            df.loc[row2,'Real']=int(real) 
                            df.loc[row2,'Duplicate']=int(duplicate) 
                            df.loc[row2,'Invalid']=int(invalid) 
                            df.loc[row2,'Absent']=1-real 
                            break

                a1+=a    
                if real==1: 
                    df2.iloc[i,row2]='P'

        df2.loc[i,'Actual Lecture Taken']=total 
        df2.loc[i,'Total Real']=real_total
        df2.loc[i,'% Attendance']=round(real_total/total,4)*100
        df.to_excel(f'{roll}.xlsx',index=False) 
    
    return df2 
    
def verify(time): 

    if time[0]==str(0): 
        a1=time[1]
    else:
        a1=time[0:2]

    if time[3]==str(0):
        a2=time[4]
    else:
        a2=time[3:5]

    time1=date(2022,int(a2),int(a1)) 
    time2=f'{time1}T{time[11:]}'
    time_range = DateTimeRange(f'{time1}T14:00:00', f'{time1}T15:00:00') 

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
    df2.to_excel('attendance_report_consolidated.xlsx',index=False) 
    print('The files have been created.')
    try:
        response=int(input("Do you want to send this file using gmail id? For 'yes' enter 1, for 'no' enter 0:")) # asking if user wants to send on given email id
        try:
            if response==1:
                send_mail('enteryourgmail@gmail.com','cs3842022@gmail.com','Please find attachment.','attendance_report_consolidated.csv is attached',
                'attendance_report_consolidated.csv','ChangeMe PASSWORD') 
        except:
            print('Error in sending an email! These could be the possible reasons:')
            print('1. Configure your email account to allow sending emails via third-party apps (Python in this case). For gmail account, use the following steps:')
            print('\ta. Go to myaccount.google.com and sign into your gmail account if required.\n\tb.Under "Security" turn on 2 step verification using your phone number. \n\tc. Go to myaccout.google.com/apppasswords and you will be asked to sign in\n\td. Under "Select app" choose "Other", and type Python in the box.\n\te.A 16 digit password appears on the screen which can be used to login here when calling the function send_mail().')
            print('2. For other email accounts, use a similar procedure or look up on the web.')
            print('3. Use the correct server and correct port. For gmail IDs, the correct server and port has been given.')
            print('4. Connect to the internet and retry.')
            print('5. The correct file path was not specified.')
    except:
        print('A non-integer value was entered!')
except:
    print('Error occured in reading file input_attendance.csv. Please change the date-format of the timestamps to dd/mm/yyyy or use a fresh input file.')

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
