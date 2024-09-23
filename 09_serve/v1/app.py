# Ben Rudinski
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

# Prediction:
# The page will display "No hablo queso!". No additional outputs or debugging features are present.
