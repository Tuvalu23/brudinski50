# Ben Rudinski | Topher's Lovers
# SoftDev
# Sep 2024

# DEMO
# basics of /static folder
import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

# I notice that this top site is essentially what we looked at yesterday with "No Hablo Queso" showing on the screen

# If I uncomment what below nothing really changes, but that is because it is a different path. If we navigate to that path we should see something different!

app.route("/static/foo.html")
def h():
    print("the __name__ of this module is... ")
    print(__name__)
    return str(random.random())

# Once I navigate to that path it says "Is this plaintext, though?"


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

