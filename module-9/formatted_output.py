# Jonathan, Davila | 7/27/2025 | 9.2 Assignment APIs
# Formats the JSON data recrieved from the API in a readable form

import json

def format_data(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)