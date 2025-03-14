from flask import Flask, render_template, redirect, url_for, request, session, flash
import sqlite3
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup
def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")
    
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)')
    conn.execute('CREATE TABLE IF NOT EXISTS blogs (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, title TEXT UNIQUE, content TEXT, FOREIGN KEY(user_id) REFERENCES users(id))')
    print("Tables created successfully")
    conn.close()

init_sqlite_db()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return render_template('index.html')

# User routes
@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            try:
                cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                flash('User registered successfully!')
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                flash('Username already taken. Please choose a different one.')
    return render_template('register.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            user = cur.fetchone()
            if user:
                session['logged_in'] = True
                session['user_id'] = user[0]
                session['username'] = user[1]
                flash('Logged in successfully!')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid credentials!')
    return render_template('login.html')

@app.route('/logout/')
@login_required
def logout():
    session.clear()
    flash('Logged out successfully!')
    return redirect(url_for('login'))

@app.route('/dashboard/')
@login_required
def dashboard():
    user_id = session['user_id']
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM blogs WHERE user_id = ?", (user_id,))
        blogs = cur.fetchall()
    return render_template('dashboard.html', blogs=blogs)

# Blog routes
@app.route('/create_blog/', methods=['GET', 'POST'])
@login_required
def create_blog():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = session['user_id']
        
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            try:
                cur.execute("INSERT INTO blogs (user_id, title, content) VALUES (?, ?, ?)", (user_id, title, content))
                conn.commit()
                flash('Blog created successfully!')
                return redirect(url_for('dashboard'))
            except sqlite3.IntegrityError:
                flash('Blog title already taken. Please choose a different one.')
    return render_template('create_blog.html')

@app.route('/edit_blog/<int:blog_id>/', methods=['GET', 'POST'])
@login_required
def edit_blog(blog_id):
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            try:
                cur.execute("UPDATE blogs SET title = ?, content = ? WHERE id = ?", (title, content, blog_id))
                conn.commit()
                flash('Blog updated successfully!')
                return redirect(url_for('dashboard'))
            except sqlite3.IntegrityError:
                flash('Blog title already taken. Please choose a different one.')
    
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM blogs WHERE id = ?", (blog_id,))
        blog = cur.fetchone()
    return render_template('edit_blog.html', blog=blog)

@app.route('/view_blog/<int:blog_id>/')
def view_blog(blog_id):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM blogs WHERE id = ?", (blog_id,))
        blog = cur.fetchone()
    return render_template('view_blog.html', blog=blog)

@app.route('/delete_blog/<int:blog_id>/')
@login_required
def delete_blog(blog_id):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM blogs WHERE id = ?", (blog_id,))
        conn.commit()
        flash('Blog deleted successfully!')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)