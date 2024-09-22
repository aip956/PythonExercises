"""
https://docs.google.com/document/d/13nvC656vZX9WPsIxr47zy9wbpWcueDu7Z3f1N0GwZqA/edit
Create env:
    python3 -m venv env
    source env/bin/activate
Install dependencies:
    pip install requests
Verify link:
    In terminal, curl -X GET https://bored-api.appbrewery.com/random
    Or in browser, https://bored-api.appbrewery.com/random




"""

import requests
def get_activity():
    response = requests.get('https://bored-api.appbrewery.com/random')
    if response.status_code == 200:
        activity_data = response.json()
        print("Activity: ", activity_data)
        return activity_data
    else:
        print("Error: ", response.status_code)
        return None

# Fetch a random activity
activity = get_activity()

# Print the activity
if activity:
    print("Activity: ", activity['activity'])
    print("Type: ", activity['type'])
    print("Participants: ", activity['participants'])
    print("Price: ", activity['price'])
    print("Accessibility: ", activity['accessibility'])
    print("Duration: ", activity['duration'])
    print("Kid Friendly: ", activity['kidFriendly'])
    print("Link: ", activity['link'])
    print("Key: ", activity['key'])



