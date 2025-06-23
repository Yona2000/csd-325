#Jonathan, Davila 06/22/2025 Assignment 4.2
#Update the code to show the menu so users can choose high or low temperatures then exit with a message. 

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import sys

filename = 'moduel_4_sitka_weather_2018_simple.csv'

#reads data from the csv file
dates, highs, lows = [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%m/%d/%Y')
            high = int(row[5])
            low = int(row[6])

            dates.append(current_date)
            highs.append(high)
            lows.append(low)

        except Exception:
            #skips the nulled date values
            continue

#function to plot temperatures
def plot_temps(dates, temps, color, title):
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
    plt.title(title, fontsize=22)
    plt.xlabel('', fontsize=13)
    fig.autofmt_xdate()
    plt.ylabel("temperature (F)", fontsize=13)
    plt.tick_params(axis='both', which='major', labelsize=13)
    plt.show()

#the menu loop
print("This is the module 4 sitka Weather chart")

while True:
    print("\n1. show high temperatures\n2. show low temperatures\n3. Exit")
    user_choice = input("Pick a number 1 or 2 or 3): ")

    if user_choice == '1':
        plot_temps(dates, highs, 'red', "daily high temperatures 2018")

    elif user_choice == '2':
        plot_temps(dates, lows, 'blue', "daily low temperatures 2018")

    elif user_choice == '3':
        print("Thanks stopping by, bye :3")
        sys.exit()

    else:
        print("Invalid choice, so select 1, 2, or 3.")
