
# Jonathan, Davila, 7/12/2025, M7 7.2 Assignment Test Cases
# Tests the module City_Functions.py

import unittest
from city_functions import city_country

class test_city_country(unittest.TestCase):

    def test_city_country(self):
        #Does the city and country Seoul, South Korea, population and language work?
        formatted_Incountry = city_country('Seoul', 'South Korea', 10025800, 'Korean')
        self.assertEqual(formatted_Incountry, 'Seoul, South Korea - population 10025800, Korean')

if __name__ == '__main__':
    unittest.main()