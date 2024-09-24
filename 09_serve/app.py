'''
Ben Rudinski
SoftDev
K09: Coding a flask app to send the output of my occupation-chooser to a webpage
2024-09-23
time spent: 0.5hr
'''

from flask import Flask
import csv
import random

app = Flask(__name__) # instaniate flask module

# copied from 06_py-csv
def occupation_reader(file_path):
    occupations = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            if len(row) == 2:  
                occupation = row[0].strip()
                percentage = float(row[1].strip())
                occupations[occupation] = percentage
    return occupations

def weighted_rand(occupations):
    occupation_list = list(occupations.keys())
    weights = list(occupations.values())
    selected_occupation = random.choices(occupation_list, weights=weights, k=1)
    return selected_occupation[0]

@app.route("/") # define a route that maps to the homepage
def show_occupations():
    file_path = 'occupations.csv'
    occupations = occupation_reader(file_path)
    selected_occupation = weighted_rand(occupations)
    
    # plain text response
    response = "Roster:\nBen Rudinski<br>"
    response += "<br>"
    response += f"Randomly Selected Occupation: {selected_occupation}<br><br>"
    response += "List of Occupations:<br>"
    
    # loop through the occupations and their percentages, adding each to the response
    for occupation, percentage in occupations.items():
        response += f"{occupation}: {percentage}%<br>"

    return response

if __name__ == "__main__":
    app.run(debug=True) # use debug mode for efficiency and ease