# Ben Rudinski
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
    
# Differences:
# - includes a common Python idiom: if __name__ == "__main__":. 
# - ensures that the Flask app is only run if the script is executed directly, not when it is imported as a module in another script.
# - If the script is imported into another file, the Flask app will not automatically run, which is a key structural improvement.