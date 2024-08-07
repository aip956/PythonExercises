
import requests
from urllib.parse import urlencode
base_url = "http://localhost:8000/send/"


def read_events_from_txt(file_path):
    events = []
    with open(file_path, mode='r') as file:
        while True:
            index = file.readline().strip()
            if not index:
                break #EOF
            event_type = file.readline().strip().split("\t")[1].strip('"')
            priority = file.readline().strip().split("\t")[1].strip('"')
            description = file.readline().strip().split("\t")[1].strip('"')
            events.append({
                "index": index,
                "event_type": event_type,
                "priority": priority,
                "description": description
            })
    return events

# Path to the file containing events
file_path = "events.txt"
# Read events from CSV
events = read_events_from_txt("events.txt")


# Send events to Kafka producer
for event in events:
    topic = event["event_type"]
    query_params = urlencode({"message": event["description"], "priority": event["priority"]})
    url = f"{base_url}{topic}?{query_params}"
    response = requests.post(url)
    if response.status_code == 200:
        print(f"Successfully sent event: {event['event_type']}")  
    else: 
        print(f"Failed to send event: {event['event_type']}, Status Code: {response.status_code}")  
    try: 
        print(f"Failed to send event: {event['event_type']}, Status Code: {response.status_code}")
    except ValueError:
        print(f"Failed to send event: {event['event_type']}, Status Code: {response.status_code}")
    print(response.json())

