from tkinter import *
import pandas as pd
import time
from tkinter import messagebox
import re
from datetime import date
from plyer import notification
import random

import matplotlib.pyplot as plt

from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from google_auth_oauthlib.flow import Flow
import re
from datetime import date
import pandas as pd
import re

import cv2
import time

#variables
curr_time = time.strftime("%H:%M:%S", time.localtime())
curr_date = date.today()

phyIndex = 99
menIndex = 99
watIndex = 0



#DATAFRAMES


#->Data for plotting
graphData = pd.DataFrame({
    'Time': [],
    'PhysicalIndex': [],
    'MentalIndex':[]
})



#->recommendation data
exerData={'Physical': ['Take a walk for 5 minutes','Cobra stretch for your back','Stretch your neck towards left and then right','blinking quickly 20 times, and then close your eyes for three deep breaths'],
      'Mental':['Place your palms on your eyes and meditate for 2 mins','Meditate for 2 minutes','Try equal breathing for 5 minutes','Listen to calm music']}

exerDf=pd.DataFrame(exerData)




#->data from Google Calendar API
flow = Flow.from_client_secrets_file(
    'client_secret.json',
    scopes=["https://www.googleapis.com/auth/calendar"],
    redirect_uri='urn:ietf:wg:oauth:2.0:oob')

    #go through the Url
auth_url, _ = flow.authorization_url(prompt='consent')

print('Please go to this URL: {}'.format(auth_url))

    # Copy the token and Paste
code = input('Enter the authorization code: ')
credentials = flow.fetch_token(code=code)

pickle.dump(credentials, open('token.pkl','wb'))
credentials = pickle.load(open('token.pkl','rb'))
service = build('calendar','v3',credentials=flow.credentials)
result = service.calendarList().list().execute()
calendar_id = result['items'][3]['id']

today = date.today()
timeCondmin = str(today) + 'T00:00:00+05:30'
timeCondmax = str(today) + 'T23:00:00+05:30'
events = service.events().list(calendarId=calendar_id,timeMin=timeCondmin,timeMax=timeCondmax).execute()

list_of_events = events['items']

event_details = {'Title' :[],'sTime' :[],'eTime' :[],'Date' :[]}
for items in list_of_events:
  event_details['Title'].append(items['summary'])

  date = re.split('T',items['start']['dateTime'])
  event_details['Date'].append(date[0])

  arr1 = re.split('T',items['start']['dateTime'])
  sTime = arr1[1].split('+')[0]
  event_details['sTime'].append(sTime)

  arr2 = re.split('T',items['end']['dateTime'])
  eTime = arr2[1].split('+')[0]
  event_details['eTime'].append(eTime)

df2 = pd.DataFrame(event_details)
df1 = df2.sort_values(by=['sTime'],ascending=True)



#FUNCTIONS

#->To show push notifications
def showNotif(message) :
    notification.notify(
            title = "Alert!",
            message=message ,
           
            # displaying time
            timeout=1
)


#-> TO plot Stats Graph
def plotGraph():
    global graphData
    graphData.plot(x="Time", y=["MentalIndex", "PhysicalIndex"], kind="line")
    plt.show()


#->To maintain water intake
def addWater() :
    global watIndex
    watIndex=float(watIndex)

    if (watIndex<4.0):
        watIndex=watIndex+0.25
        watIndex = ("%.2f" % watIndex)
    else :
        watIndex=4.0
        watIndex = ("%.2f" % watIndex)
        showNotif("Daily water intake complete!")



#TKINTER GUI



window = Tk()
window.geometry("420x520")
window.title("FitNotify")
window.config(background="#000000")

p1 = PhotoImage(file = 'icon.png')
window.iconphoto(False, p1)

titleText = Label (window, text = "FitNotify" , font=('Comic Sans MS', 40, 'bold'), fg='#FFFFFF', bg='#000000')
titleText.place(x=70, y=45)

meetingsText = Label (window, text="Meetings", font=('Comic Sans MS', 20, 'bold'), fg='#FFFFFF', bg='#000000')
meetingsText.place(x=50, y=135)

tempY=180
for ind in df1.index:
    tempTitle=Label(window, text = df1['Title'][ind],font=('Comic Sans MS', 10, 'bold'), fg='#FFFFFF', bg='#000000')
    tempTitle.place(x=50, y=tempY)
                    
    tempDate=Label(window, text = df1['Date'][ind],font=('Comic Sans MS', 10, 'bold'), fg='#FFFFFF', bg='#000000')
    tempDate.place(x=200, y=tempY)
                   
    tempsTime=Label(window, text = df1['sTime'][ind],font=('Comic Sans MS', 10, 'bold'), fg='#FFFFFF', bg='#000000')
    tempsTime.place(x=290, y=tempY)
    
    tempY=tempY+30

waterTitle = Label(window, text = "Water Intake" , font=('Comic Sans MS', 16, 'bold'), fg='#FFFFFF', bg='#000000')
waterTitle.place(x=30, y=tempY+70)



waterButton = Button(window, text="Add Water", command=addWater)
waterButton.place(x=30, y=tempY+180)


statsButton = Button(window, text="show stats", command=plotGraph)
statsButton.place(x=282, y=tempY+200)



phyTitle=Label (window, text = "Physical Index" , font=('Comic Sans MS', 15, 'bold'), fg='#FFFFFF', bg='#000000')
phyTitle.place(x=250, y=tempY+40)



menTitle=Label (window, text = "Mental Index" , font=('Comic Sans MS', 15, 'bold'), fg='#FFFFFF', bg='#000000')
menTitle.place(x=250, y=tempY+110)



#ScreenTime Capture Using webcam (variables)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
cap = cv2.VideoCapture(0)

work = 0
startTime = time.time()
currTime = startTime
flag = 0




#Main loop for updating data and using webcam

def updateInfo() :
    #updating the indexes
    global phyIndex
    global menIndex
    global watIndex
    
    global curr_time
    curr_time = time.strftime("%H:%M:%S", time.localtime())


    global df1
    for index in range(len(df1)):
        if curr_time == df1.eTime[index]:
              phyIndex=phyIndex-10
              menIndex=menIndex-20
              messagebox.showinfo("reminder", "Hope you had a great meeting! Time for a 10 mins break")


    
    phyInLabel=Label (window, text = phyIndex , font=('Comic Sans MS', 20, 'bold'), fg='#FFFFFF', bg='#000000')
    phyInLabel.place(x=300, y=tempY+70)

    menInLabel=Label (window, text = menIndex , font=('Comic Sans MS', 20, 'bold'), fg='#FFFFFF', bg='#000000')
    menInLabel.place(x=300, y=tempY+140)

    waterInLabel=Label (window, text = str(watIndex) + "L", font=('Comic Sans MS', 20, 'bold'), fg='#FFFFFF', bg='#000000')
    waterInLabel.place(x=30, y=tempY+100)

    waterRemLabel=Label (window, text = "Remaining:"+ str("%.2f" % (float(4.0)-float(watIndex)))+"L", font=('Comic Sans MS', 10, 'bold'), fg='#FFFFFF', bg='#000000')
    waterRemLabel.place(x=30, y=tempY+150)

    
    global face_cascade
    global cap
    global work
    global startTime
    global currTime
    global flag
    global graphData

    
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)

    if len(faces) == 0:
        pass
        

        

    else:
        work+=1
        if (work>=200):
            work=0
            phyIndex-=5
            menIndex-=10
            showNotif("Take a break")
            
            curr_time = time.strftime("%H:%M:%S", time.localtime())
            tempDf=pd.DataFrame({
                'Time': [str(curr_time)],
                'PhysicalIndex': [phyIndex],
                'MentalIndex':[menIndex]
            })

            graphData = pd.concat([graphData, tempDf])
            
            
        


        for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    
    cv2.imshow('img', img)

    if (phyIndex<=50):
        r=random.randint(0,len(exerDf)-1)
        showNotif(str(exerDf['Physical'][r]))
        phyIndex=phyIndex+10
        
    if (menIndex<=50):
        r=random.randint(0, len(exerDf)-1)
        showNotif(str(exerDf['Mental'][r]))
        menIndex=menIndex+15
        
    
    
    
        
    window.after(1, updateInfo)


window.after(1, updateInfo)
window.mainloop()



