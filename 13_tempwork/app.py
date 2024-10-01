# Endrit Idrizi
# Minerals FC - Endrit, Ben, Vedant
# SoftDev 
# K13: CSV file parsing, flask, displaying to HTML as a table with links 
# 2024-10-1
# Time Spent : 1.5 Hours 

import random
import csv
from flask import Flask, render_template

app = Flask(__name__)

# read csv and return dictionary with job data
def readfile(f):
    d = {}
    with open(f, 'r') as listfile:
        reader = csv.DictReader(listfile)
        for row in reader:
            job = row['Job Class']
            if job == "Total":
                continue # skip total
            percent = float(row['Percentage'])
            link = row['Link'] # read links as well{'percentage': percent, 'link': link}
            d[job] = {'percentage': percent, 'link': link}
    return d        
            
# randomly select occupation based on weighted chance
def sel(d):
    return random.choices(list(d.keys()), weights=[v['percentage'] for v in d.values()], k=1)[0]

@app.route("/wdywtbwygp")
def page():
    occupations = readfile("data/occupations.csv")
    random_job = sel(occupations)
    return render_template(
        "tablified.html",
        tnpg_roster="Minerals FC - Endrit, Ben, Vedant",
        occupations=occupations,
        random_job=random_job
    )
    
if __name__ == "__main__":
    app.debug = True # comment out later
    app.run()
