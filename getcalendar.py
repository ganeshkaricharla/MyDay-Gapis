from googleapiclient.discovery import build
import os
import Oauth
import pickle

def get_servicecalendar():
    if not os.path.exists('token.pkl'):
        Oauth.get_credentials()
    credentials =pickle.load(open("token.pkl","rb"))
    servicecal = build("calendar","v3" ,credentials=credentials)
    return servicecal

def get_calendarlist(servicecal):
    calendar_list = servicecal.calendarList().list().execute()
    MyAcademics = calendar_list['items'][3]
    Calendar_id =MyAcademics['id']
    return Calendar_id

def get_todayevents(servicecal,NOW,NOWMAX,Cid):
    MyAcademicEvents = servicecal.events().list(calendarId=Cid,timeMin=NOW,timeMax=NOWMAX,singleEvents=True,orderBy='startTime').execute()
    today_events={}
    count_events=0
    for i in MyAcademicEvents['items']:
        Eventname=i['summary']
        EventTimes=i['start']['dateTime'][11:19]
        Eventtimee=i['end']['dateTime'][11:19]
        today_events[Eventname]=(EventTimes,Eventtimee)
        count_events+=1
    return list([count_events,today_events])
