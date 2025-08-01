# Jonathan, Davila | 7/26/2025 | 9.2 Assignment APIs

import requests
import json

def get_data_response():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response.status_code)
    return response.json()


def format_data(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

data = get_data_response()
format_data(data)





