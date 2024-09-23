# Ben Rudinski
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #where will this go?
    return "No hablo queso!"

app.run()

# Differences:
# - The line print(__name__) has been added inside the route function.
# - print("about to print __name__...") is also included before printing __name__.

# Prediction:
# - The string "No hablo queso!" will still be returned to the browser, but now you'll see two additional lines printed in the terminal whenever you load the page.
