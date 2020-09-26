import datetime
import getcalendar
import getmail
import htmlmake
import os


NOW = now = datetime.datetime.utcnow().isoformat() + 'Z'
#NOW = "2020-09-25T01:00:00.00303Z"  #tospecify certaindate for check
NOWMAX = NOW[0:11]+"23:59:59.000000Z"

servicecal=getcalendar.get_servicecalendar()
today_events=getcalendar.get_todayevents(servicecal,NOW,NOWMAX,getcalendar.get_calendarlist(servicecal))

servicemail=getmail.get_servicemail()
unread_mails=getmail.get_unreadmail(servicemail)

is_success=htmlmake.make_html(today_events[0],unread_mails[0],today_events[1],unread_mails[1])

if is_success:
    os.system("C:\\Users\\ganes\\Desktop\\myDaymake.html")

