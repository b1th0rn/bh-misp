import requests, sys

def get_events_list(api_url, api_key):
    try:
        # Send a GET request to the API
        response = requests.get(api_url, timeout=15, headers={"Authorization": api_key, "Accept": "application/json", "Content-Type": "application/json"}, verify=False)
        
        for event in response.json():
            #print(f"Event ID: {event['id']}, Event Info: {event['info']}")
            print(f"Event ID: {event['id']}")

    except requests.exceptions.RequestException as e:
        print(f"[-] API is DOWN: {api_url} - Error: {e}")

def get_event_details(api_url, api_key, event_id):
    try:
        # Send a GET request to the API
        response = requests.get(f"{api_url}/{event_id}", timeout=15, headers={"Authorization": api_key, "Accept": "application/json", "Content-Type": "application/json"}, verify=False)
        
        # Print the event details
        print(response.json())

    except requests.exceptions.RequestException as e:
        print(f"[-] API is DOWN: {api_url} - Error: {e}")

if __name__ == "__main__":
    get_events_list(f"{sys.argv[1]}/events", sys.argv[2])
    # get_event_details("https://misp.local/events", sys.argv[1], sys.argv[2])
