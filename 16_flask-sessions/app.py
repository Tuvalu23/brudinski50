'''
Ben Rudinski
Topher Forever
SoftDev
K16: Take and Keep
2024-10-09
time spent: 1 hr
'''
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'Topher1234' # key used for session management

team_name = "Topher Alone"
roster = ["Ben Rudinski"]

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('welcome'))
    return render_template('login.html', team_name=team_name, roster=roster)

@app.route('/login', methods=['POST']) # only post
def login():
    username = request.form.get('username')
    session['username'] = username # store the username in a session
    print(f"Debug Message: User {username} has logged in!")
    return redirect(url_for('welcome'))
    
@app.route('/welcome')
def welcome():
    if 'username' in session:
        username = session['username']
        greeting = f"Hello, {username}! Welcome to this beautiful Flask App!"
        method_used = request.method
        
        explanation = """
        Now you're logged in! You will remain logged in until you log out.
        This Flask app uses sessions, which are managed via cookies. Your session data is stored on the server,
        and a session cookie is sent to your browser.
        """
        
        return render_template('response.html', username=username, method=method_used, 
                               greeting=greeting, explanation=explanation, 
                               team_name=team_name, roster=roster)
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    username = session.pop('username', None) # remove user from session
    print(f"DEBUG: User {username} logged out!")
    return render_template('logout.html', team_name=team_name, roster=roster)
    
        
if __name__ == '__main__':
    app.run(debug=True)
