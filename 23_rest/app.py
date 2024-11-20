'''
Ben Rudinski
TopherAPI
SoftDev
K23: RESTful Journey Skyward -- Use an API key to display information from the NASA API
2024-11-20
time spent: 1 hr
'''
from flask import Flask, render_template, request
import urllib.request # request api
import json # send api

app = Flask(__name__)

team_name = "TopherAPI"
roster = ["Ben Rudinski + Tiffany Yang"]

# read nasa api key from file
with open("key_nasa.txt", "r") as topher:
    api_key = topher.read().strip()

@app.route('/')
def main():
    
    # api endpoint for picture of the day
    nasa_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    
    # parse JSON response and make request
    try:
        response = urllib.request.urlopen(nasa_url)
        data = json.loads(response.read())
        print(json.dumps(data, indent=4)) # debug to print API response
    except Exception as e:
        data = {"error": str(e)}
        print(f"There was an error fetching your data from NASA API: {e}")
    
    #extract the data
    image_url = data.get('url')
    explanation = data.get('explanation')
    title = data.get('title')
    
    return render_template('main.html', team_name=team_name, roster=roster, image_url=image_url, explanation=explanation, title=title)

if __name__ == '__main__':
    app.run(debug=True)