# Ben Rudinski
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # creates instance of the flask class

@app.route("/")                # tells the Flask app which URL should trigger the associated function. In this case, the "/" route corresponds to the home page or root URL of the application
def hello_world():
    print(__name__)            # prints the name of the current module. If the script is run directly, __name__ will be "__main__".
    return "No hablo queso!"   # sends this string as the response to the web browser. It’s what users will see when they visit the root URL.

app.run()                      # starts the Flask development server, which will run the web application locally so you can test it.

