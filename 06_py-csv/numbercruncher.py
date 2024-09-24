'''
Ben Rudinski
Novillo
SoftDev
K06: CSV Reading -- Reading a CSV file and turning it into a dictionary and then implementing weighted-random-chance to select one at random
2024-09-20
time spent: 1.5 hr
'''

import csv
import random

# function to read the CSV and return a dictionary of occupations and their percentages
def occupation_reader(file_path):
    occupations = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)  # Uue csv.reader to handle quoted lines bc they exist in our file
        next(csv_reader)  # Sskip header
        for row in csv_reader:
            if len(row) == 2:  # check if we have exactly two elements (occupation, percentage)
                occupation = row[0].strip()
                percentage = float(row[1].strip())
                if occupation.lower() != "total":
                    occupations[occupation] = percentage
    return occupations

# function to randomly select an occupation weighted by percentages
def weighted_rand(occupations):
    occupation_list = list(occupations.keys())
    weights = list(occupations.values())
    selected_occupation = random.choices(occupation_list, weights=weights, k=1)
    return selected_occupation[0]

if __name__ == "__main__":
    file_path = 'occupations.csv'
    occupations = occupation_reader(file_path)
    selected_occupation = weighted_rand(occupations)
    print(f"Random Occupation: {selected_occupation}")
