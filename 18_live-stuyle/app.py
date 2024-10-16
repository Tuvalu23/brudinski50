'''
Ben Rudinski
Topher Alone
SoftDev
K18: Styling a Flask App
2024-10-15
time spent: 1 hr
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)