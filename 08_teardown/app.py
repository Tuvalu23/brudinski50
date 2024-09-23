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


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

# The maih function in python has simillar synthax with if "__name__"

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?

#  Could be a file path, also I see an @ symbol so it could be ran in terminal. Perhaps its the route of a path or website/application

def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?

 # It will print to the terminal/constole and it will print __main__
 
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

# It will enter in the browser when you enter the app route "/". This is because flask's routing system send the return value of the function as an HTTP request

app.run()                                # Q5: Where have you seen similar constructs in other languages?

# This looks like common java functions or processing functions


