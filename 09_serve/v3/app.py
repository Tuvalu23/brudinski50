# Ben Rudinski
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)                   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

# Differences:
# - The line app.debug = True is added, which enables Flask's debug mode.
# - provides extra error information and automatically restarts the server when code changes are detected.

# Prediction:
# - Everything from v2 still happens, but Flask will automatically reload when you edit the code, and debugging information will be more detailed if errors occur.