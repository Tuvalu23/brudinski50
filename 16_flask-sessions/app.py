'''
Ben Rudinski
Topher Forever
SoftDev
K16: Take and Keep
2024-10-09
time spent: 1 hr
'''
from flask import Flask, render_template, request, url_for, session

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

if __name__ == '__main__':
    app.run(debug=True)
