import datetime
import json

import schedule
import time
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dateutil import parser
from LibRizz import main
import requests





# Set up the Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'creds.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('calendar', 'v3', credentials=credentials)

# Replace 'primary' with your specific calendar ID
CALENDAR_ID = '3be6a595c0e6c476c94e9e42011fd86bb4bb98729f71061bbc1fb1b0bfa7bcea@group.calendar.google.com'


def get_settings():
    with open('settings.json', 'r') as file:
        data = json.load(file)
    return data

def alert(title, message):
    url = "https://api.pushover.net/1/messages.json"
    settings = get_settings()
    data = {
        "token": settings['pushover_token'],
        "user": settings['pushover_user'],
        "title": title,
        "message": message
    }
    try:
        headers = {
            "Content-type": "application/x-www-form-urlencoded"
        }

        response = requests.post(url, data=data, headers=headers)
        print(response.status_code)
        print(response.text)
    except Exception as e:
        print("[ERROR] Error sending alert : {}".format(e))
        #print(e)

def check_and_update_calendar():
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    one_week_later = (datetime.datetime.utcnow() + datetime.timedelta(weeks=1)).isoformat() + 'Z'

    events_result = service.events().list(calendarId=CALENDAR_ID, timeMin=now, timeMax=one_week_later,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    print("Found {} events".format(len(events)))

    for event in events:
        if '[CONFIRMED]' not in event['summary']:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))
            start_time = parser.isoparse(start)
            end_time = parser.isoparse(end)
            duration = (end_time - start_time).total_seconds() / 3600
            print(f"Event: {event['summary']}, Start: {start_time}, Duration: {duration} hours")

            settings = get_settings()

            print("{} nd {}".format(type(start_time), type(end_time)))
            try:
                room = main(start_time, end_time,settings['user_nid'], settings['user_pass'], settings['user_pid'], settings['user_group'], settings['user_lname'])
                print(room)
                # Update the event
                event['summary'] = '[CONFIRMED] ' + event['summary']
                event['location'] = str(room)  # Update with the desired location

                updated_event = service.events().update(calendarId=CALENDAR_ID, eventId=event['id'], body=event).execute()
                print(f"Updated Event: {updated_event['summary']} at {updated_event['location']}")
                alert("Booked Room", f"Booked room {room} for {duration} hours on {start_time.strftime('%A, %B %d, %Y')}")
            except Exception as e:
                alert("Error", "There was an error booking a room. Please check the calendar. Error: {}".format(e))
                print("Error booking room")


time.sleep(2)
print("Starting")
#check_and_update_calendar()



# Schedule the script to run every hour
schedule.every(15).minutes.do(check_and_update_calendar)

check_and_update_calendar()
while True:
    schedule.run_pending()
    time.sleep(1)