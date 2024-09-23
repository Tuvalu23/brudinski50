'''
Ben Rudinski
Novillo
SoftDev
K08: Flask Questions
2024-09-21
time spent: 1
'''

'''
DISCO:
<note any discoveries you made here... no matter how small!>

QCC:
0. What is flask?
1. Why do we need flask?
2. Why was it named flask?
3. Will we ever use flask in this class?
4. Who created flask, in what year?
5. Are there any alternatives to flask?
 ...

INVESTIGATIVE APPROACH:
We set about this task by finding points of reference to understand what each function/terminology meant. 
'''


from flask import Flask  # importing the Flask class from the flask package

app = Flask(__name__)  # q0: where have you seen similar syntax in other langs?

# this syntax is similar to the main function construct in many languages, such as java and c++
# the `__name__` variable in python is used to determine if the file is being run directly or imported.

@app.route("/")  # q1: what points of reference do you have for the meaning of '/'?

# the `/` typically represents the root path of a web application, as it does in URLs. 
# the `@` symbol is a decorator in python, which modifies the function that follows it. 
# in this case, it sets up the routing for the home page of the web app.

def hello_world():
    print(__name__)  # q2: where will this print to? q3: what will it print?

    # this will print to the terminal/console when the function is triggered by a browser request.
    # it will print "__main__" since the script is being executed directly.

    return "No hablo queso!"  # q4: will this appear anywhere? how do you know?

    # this string will be displayed in the browser when someone accesses the "/" route.
    # flask’s routing system sends the return value of the function as the HTTP response content.

app.run()  # q5: where have you seen similar constructs in other languages?

# similar constructs exist in java, where the `main` function serves as an entry point.
# app.run() starts the flask development server, allowing the web app to handle requests.

