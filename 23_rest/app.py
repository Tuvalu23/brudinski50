'''
Ben Rudinski
TopherAPI
SoftDev
K23: Rest -- Use an API key to display information from the (NASA) API
2024-11-20
time spent: 1 hr
'''
from flask import Flask, render_template, request

app = Flask(__name__)

team_name = "TopherAPI"
roster = ["Ben Rudinski + Tiffany Yang"]

@app.route('/')
def main():
    return render_template('main.html', team_name=team_name, roster=roster)

if __name__ == '__main__':
    app.run(debug=True)