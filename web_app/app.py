"""This is our web server we are using flask"""

from flask import Flask, config, render_template, request, redirect
import sys
import os


# Imports from the 'engine' folder in the parent directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(BASE_DIR, '..'))

sys.path.append(project_root)

from engine.database import SimpleDB


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# We point it to the same 'data' folder so it sees my REPL data
data_path = os.path.join(project_root, 'data')
db = SimpleDB(data_dir=data_path)

@app.route('/')
def index():
    #The database to check the 'data/' folder for new files 
    db.autoload_tables()


    # Demonstrates READ: Fetch data from a table named 'users'
    # Using our custom engine's execute method!

    rows = db.execute("SELECT * FROM users")

    # If the table doesn't exist yet, rows will be an error string
    if isinstance(rows, str):
        rows = []

    return render_template('index.html', rows=rows)

@app.route('/add', methods=['POST'])
def add_user():
    # Demonstrate CREATE: Get data from a web form 
    user_id = request.form['id']
    name = request.form['name']

    # Execute an INSERT using your custom RDBMS
    db.execute(f"INSERT INTO users VALUES ({user_id}, '{name}')")

    return redirect('/')

if __name__ == '__main__':
    #Ensure a 'users' table exists for the Demo 
    db.execute("CREATE TABLE users (id, name)")
    app.run(debug=True, port=5000)
