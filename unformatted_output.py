# Jonathan, Davila | 7/27/2025 | 9.2 Assignment APIs
# Sends a get request to the API url then prints the status code and returns the response data in JSON

import requests

def get_data_response(url):
    response = requests.get(url)
    print(response.status_code)
    return response.json()
