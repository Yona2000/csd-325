# Jonathan, Davila | 7/27/2025 | 9.2 Assignment APIs
# Created a main with other supporting modules to keep the code organized while still meeting the purpose of getting data from the API to show unformatted and formatted JSON output 

from connections import  Api_Url_Open_Notify_Astronauts, Api_Url_Poke_Api
from unformatted_output import get_data_response
from formatted_output import format_data

# Call the function to get the data from the API
data = get_data_response(Api_Url_Poke_Api)

# wraps my print statments and input prompt into one function
def output_shown(unformatted_data, formatting):
    print('\n*Unformatted Output*\n')
    print(unformatted_data)

    input("Hit Enter for the formated output:  ")

    print('\n**Formatted Output**\n')
    formatting(unformatted_data)

# Call the output function, passing in the data and the formatting function
output_shown(data, format_data)


