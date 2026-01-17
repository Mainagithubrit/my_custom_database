"""This is our web server we are using flask"""

from flask import Flask, render_template, request, redirect
import sys
import os

# Imports from the 'engine' folder in the parent directory

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine.database import SimpleDB

app = Flask(__name__)

#Initializing our custom RDBMS
# We point it to the same 'data' folder so it sees my REPL data
db = SimpleDB(data_dir="../data")

@app.route('/')
def index():
# Demonstrates READ: Fetch data from a table named 'users'
# Using our custom engine's execute method!

rows = db.execute("SELECT * FROM users")

# If the table doesn't exist yet, rows will be an error string
if issinstance(rows, str):
    rows = []

    return render_template('index.html', rows=rows)

@app.route('/add', methods=['POST'])

