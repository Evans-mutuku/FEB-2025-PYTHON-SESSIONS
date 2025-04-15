import requests

response = requests.get('https://api.github.com/events')

if response.status_code == 200:  # Check if the request was successful
    events = response.json()  # Parse the JSON response
    if events:  # Ensure there is at least one event
        print(events[0])  # Print the first event
    else:
        print("No events found.")
else:
    print(f"Failed to fetch events. Status code: {response.status_code}")
