s1='''<!DOCTYPE html>
<html>
    <head>
        <style>
            body
            {
                margin:0;
                background-color: #4444ff;
            }
            .events
            {
                background-color: #e8f809ec;
                border: 2px solid grey;
                width: 59.25%;
                margin: 2px;
                float: right;
            }
            .unread
            {
                background-color: white;
                border: 2px solid grey;
                width:39.25%;
                margin: 2px;
                float: left;
            }

            .evnt
            {
                width: 90%;
                height: auto;
                border: 1px solid black;
                margin: 2vh 2vw;
            }
            .unread_msg
            {
                width: 90%;
                height: auto;
                border: 1px solid black;
                margin: 0.5vh 2vw;
                background-color: chocolate;
            }
            .unread_notify
            {
                background-color: red;
                width: 100%;
            }
            .unread_notify p
            {
                color: white;
                text-align: center;
            }
            a
            {
                color: white;
                text-decoration: none;
            }
            .evnt ,.unread_msg
            {
                font-size: medium;
                font-weight: 600;
                font-family: Verdana, Geneva, Tahoma, sans-serif;
                color: rgba(14, 93, 196, 0.952);
            }
            .unread_msg p
            {
                margin: 2px;
                color: white;
            }
            .evnt p
            {
                font-size:large;
                text-align: center;
                display: inline-block;
                margin:18px;
                margin-right: 60px;
            }
            .evnt_time
            {
                display: inline-block;
            }

        </style>
    </head>
<body>
        <div class="events">
            <h1 style="text-align: center;">Today Events</h1>'''

s2='''<div class="unread_notify"><p>To Change Event Go to <a href="https://calendar.google.com">Calendar.google.com</a></p></div>
        </div>
        <div class="unread">
            <h1 style="text-align: center;">Unread Messages</h1>'''

s3='''<div class="unread_notify"><p>To Read mails Go to <a href="https://mail.google.com">mail.google.com</a></p></div>
        </div>

    </body>
</html>'''

def make_html(CE,CU,today_events,unread_mails):
    with open("C:\\Users\\ganes\\Desktop\\myDaymake.html",'w') as f:
        f.write(s1)
        f.write('<div class="unread_notify"><p>You have '+str(CE)+' Events to do</p></div>\n')
        for i in today_events:
            f.write('<div class="evnt"><p>'+str(i)+" From "+str(today_events[i][0])+" To"+ str(today_events[i][1]) +'</p></div>\n')
            #'</p>\n<p class="evnt_time">'+
        f.write(s2)
        f.write('\n<div class="unread_notify"><p>You have '+ str(CU) +' unread messages</p></div>\n')
        for i in unread_mails:
            f.write('<div class="unread_msg"><p>Mail From '+ str(i)+'</p></div>')
        f.write(s3)

    return True

    