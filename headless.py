import datetime
import json

import schedule
import time
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dateutil import parser
from LibRizz import main



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

def check_and_update_calendar():
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    one_week_later = (datetime.datetime.utcnow() + datetime.timedelta(weeks=1)).isoformat() + 'Z'

    events_result = service.events().list(calendarId=CALENDAR_ID, timeMin=now, timeMax=one_week_later,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    for event in events:
        if '[CONFIRMED]' not in event['summary']:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))
            start_time = parser.isoparse(start)
            end_time = parser.isoparse(end)
            duration = (end_time - start_time).total_seconds() / 3600
            print(f"Event: {event['summary']}, Start: {start_time}, Duration: {duration} hours")

            settings = get_settings()

            try:
                room = main(start_time, end_time,settings['user_nid'], settings['user_pass'], settings['user_pid'], settings['user_group'], settings['user_lname'])
                # Update the event
                event['summary'] = '[CONFIRMED] ' + event['summary']
                event['location'] = str(room)  # Update with the desired location

                updated_event = service.events().update(calendarId=CALENDAR_ID, eventId=event['id'], body=event).execute()
                print(f"Updated Event: {updated_event['summary']} at {updated_event['location']}")
            except:
                pass






check_and_update_calendar()


'''
# Schedule the script to run every hour
schedule.every().hour.do(check_and_update_calendar)

while True:
    schedule.run_pending()
    time.sleep(1)
'''