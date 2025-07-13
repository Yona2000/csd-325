
# Jonathan, Davila, 7/12/2025, M7 7.2 Assignment Test Cases
# Write a function that accepts two parameters that returns a single string in the form of city, country

# Formatted string using the "city, country, population" parameters
def city_country(city, country, population=None, language=None):
    if population:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    elif language:
        return f"{city}, {country}, {language}"
    else:
        return f"{city}, {country}"
    
# Blocks the execution of the imput prompts when the file is imported into test_cities.py
if __name__ == '__main__':

# Call the function three times
    print(city_country("Rotterdam", "Netherlands"))
    print(city_country("Hangzhou", "China", population=8591040))
    print(city_country("Seoul", "South Korea", population=10025800, language="Korean"))

 # Prompts the user on how to quit the program
    print("Press the spacebar then hit Enter to quit this program.")

    while True:
        city = input("\nGive me a city name: ")
        if city == "":
            break

        country = input("\nGive me the country that city resides in, please: ")
        if country == "":
            break

        population = input("\nGive me the population of that city, if not hit Enter to skip!:").replace(",", "")

        language = input("\nGive me the national language of said country, if not hit Enter to skip!:")

        formatted_InCountry = city_country(city, country, language, population)
        print(f"IncountryInfo: {formatted_InCountry}")

   
