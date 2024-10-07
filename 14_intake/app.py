# Ben Rudinski
# SoftDev
# October 2024

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

import testmod0

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
 * Some will work as written;
 *  ...other sections will not. 

TASK:
 Predict which.
 1. Devise simple tests to isolate components/behaviors.
 2. Execute your tests.
 3. Process results.
 4. Findings yield new ideas for more tests? Yes: do them.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

'''
Test 1: Changing Nothing
- The flask module prompts you to enter a username and then on the screen I see the text "Waaaa hooo HAAAH" after submitting the query

Test 2: Uncommenting Everything
- The flask module still prompts you to enter a username and then on the screen I see the text "Waaaa hooo HAAAH" after submitting the query

Test 3: Replace return "Waaaa hoo HAAAH" with request.args
- I see long statements in my terminal respresenting our diagnostic print statements

Test 4: Handling Empty Form Submissions
- What happens if the form is submitted without a username? I see a KeyError in the terminal when trying to access request.args['username'] directly.
- To handle this, we should use request.args.get('username') instead of request.args['username'] in the code. This way, it returns None if 'username' is not present, avoiding a crash due to a KeyError.

Test 5: Displaying the Username on the Page
- Replaced the return "request.args" statement in the /auth route with return f"Hello, {request.args.get('username')}!" to display the submitted username on the page.
- After this change, the app now displays the username input after form submission

Test 6: Handling POST Requests
- Modified the form to use method="POST" and changed the @app.route("/auth") to accept POST requests (methods=['GET', 'POST']).
- Flask captures the form data via request.form instead of request.args when using POST.

PROTIP: Use request.method to check if the form is submitted using GET or POST.

Additional Considerations:
- Add more test cases as you expand the functionality of the app. For example, testing edge cases like submitting invalid data, handling empty input fields, and validating form submissions.
- Refactor code to make it more modular as the app grows, reducing duplication and ensuring cleaner code.

Test Results Summary:
- The app is fully functional with the modifications and can now handle username input dynamically. The form submits data via GET or POST (depending on how it's set), and the output is displayed on the page after form submission. 
- Debugging tools and print statements have been helpful in identifying issues and ensuring data flow is correct.


'''

# route for handling form submission from the login page
@app.route("/")
def disp_loginpage():
    # print statements for debugging and understanding request and app objects
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")  # request.args captures query parameters (form data)
    print(request.args)  # print the full dictionary of query parameters
    print("***DIAG: request.headers ***")  # print request headers for additional debug info
    return render_template('login.html')  # serve the login.html page when this route is accessed

# route for handling form submission from the login page
@app.route("/auth", methods=['GET', 'POST'])  # handle both GET and POST requests
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    
    if request.method == 'POST':  # check if the form is submitted using POST
        username = request.form.get('username')  # use request.form for POST method
    else:
        username = request.args.get('username')  # use request.args for GET method
    
    print("***DIAG: request.args ***")
    print(request.args)  # for GET request debugging
    print("***DIAG: request.form ***")
    print(request.form)  # for POST request debugging
    print("***DIAG: username  ***")
    print(username)
    print("***DIAG: request.headers ***")
    print(request.headers)
    
    if not username:  # handle empty form submissions
        return "Please provide a username!"
    
    return f"Hello, {username}!"  # display the username entered by the user on the page

if __name__ == "__main__":
    app.debug = True  # enable debug mode for better error reporting and auto-restart on changes
    app.run()  # run the Flask app 