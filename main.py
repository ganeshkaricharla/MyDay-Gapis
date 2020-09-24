import datetime
import getcalendar
import getmail


NOW = now = datetime.datetime.utcnow().isoformat() + 'Z'
NOW = "2020-09-25T01:00:00.00303Z"  #tospecify certaindate for check
NOWMAX = NOW[0:11]+"23:59:59.000000Z"

servicecal=getcalendar.get_servicecalendar()
today_events=getcalendar.get_todayevents(servicecal,NOW,NOWMAX,getcalendar.get_calendarlist(servicecal))
print(today_events)

servicemail=getmail.get_servicemail()
unread_mails=getmail.get_unreadmail(servicemail)
print(unread_mails)