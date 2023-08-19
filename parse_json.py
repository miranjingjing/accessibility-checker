import requests, os
from dotenv import load_dotenv

#  WAVE api key
load_dotenv()
api_key = os.getenv("API_KEY")
url = os.getenv("URL")
report_type = 1

# get data from WAVE api in json format

def pretty_print():
    # store general errors
    errors_array = []

    # store contrast errors
    contrast_errors_array = []

    # store other alerts
    alerts_array = []
    
    response = requests.get(f'https://wave.webaim.org/api/request?key={api_key}&reporttype=2&url={url}')
    if response.ok:
        data = response.json()
        
        # credits remaining
        print("Credits Remaining:")
        print(data['statistics']['creditsremaining'])

        # STORE GENERAL ERRORS
        errors = data["categories"]["error"]["items"]
        for type, item in errors.items():
            error_item = {
                "id": item["id"],
                "description": item["description"],
                "count": item["count"]
            }
            errors_array.append(error_item)
        
        # print general errors
        print("GENERAL ERRORS:")
        for error in errors_array:
            print("Type of Error: " + error["id"])
            print("Error Description: " + error["description"])
            print("Number of Errors: " + str(error["count"]))
            print()

        # STORE CONTRAST ERRORS
        contrast_errors = data["categories"]["contrast"]["items"]
        for type, item in contrast_errors.items():
            error_item = {
                "id": item["id"],
                "description": item["description"],
                "count": item["count"]
            }
            contrast_errors_array.append(error_item)
        
        # print contrast errors
        print("CONTRAST ERRORS")
        for error in contrast_errors_array:
            print("Type of Error: " + error["id"])
            print("Error Description: " + error["description"])
            print("Number of Errors: " + str(error["count"]))
            print()

        # store alerts
        alerts = data["categories"]["alert"]["items"]
        for type, item in alerts.items():
            error_item = {
                "id": item["id"],
                "description": item["description"],
                "count": item["count"]
            }
            alerts_array.append(error_item)
        
        # print alerts
        print("ALERTS")
        for error in alerts_array:
            print("Type of Error: " + error["id"])
            print("Error Description: " + error["description"])
            print("Number of Errors: " + str(error["count"]))
            print()

    return errors_array, contrast_errors_array, alerts_array