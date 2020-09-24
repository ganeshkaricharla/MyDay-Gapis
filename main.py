import datetime
import getcalendar
import getmail


NOW = now = datetime.datetime.utcnow().isoformat() + 'Z'
NOW = "2020-09-25T01:00:00.00303Z"  #tospecify certaindate for check
NOWMAX = NOW[0:11]+"23:59:59.000000Z"

servicecal=getcalendar.get_servicecalendar()
getcalendar.get_todayevents(servicecal,NOW,NOWMAX,getcalendar.get_calendarlist(servicecal)[1])

servicemail=getmail.get_servicemail()
getmail.get_unreadmail(servicemail)