				# my_custom_database

 Using python and Flask, I have created a custom database that uses CRUD to modify different sets of data stored in our database. I has an interactive REPL that uses SQL syntax to manipulate data in my database.I will have a front-end for showing my tables  in a web-app that is why I use flask as a framework.

Some of the imports that I have used are:
 - Flask -  to be able to use flask web framework
 - re - (regular expression) will act as my parser, this will be used to identify keywords
 - json - for storing my data
 - cmd - this is what I use to create my REPL

 Below is my file system and what each file does:
	 my_custom_db/
├── engine/                 # Core RDBMS Logic
   ├── __init__.py
   ├── database.py         # Main engine class (manages multiple tables)
   ├── table.py            # Table logic (CRUD, Primary Keys, Unique keys)
   ├── index.py            # Indexing logic (B-Tree or Hash Map)
   └── parser.py           # SQL string to command translator
├── data/                   # Physical storage (created automatically)
   ├── users.json          # Tables stored as JSON or binary files
   └── orders.json
├── web_app/                # Flask/FastAPI Web Demonstration
   ├── static/             # CSS and JS files
   ├── templates/          # HTML files (index.html, table_view.html)
   └── app.py              # Web server entry point
├── main_repl.py            # Interactive CLI mode
└── requirements.txt        # Flask, sqlparse, rich
  
How to run the REPL:
	- First you open the file 'my_custom_db'
	- Type the command "Python main_repl.py"
	- Once you press enter the REPL will be active, you can now start entering commands.
	-  To exist the REPL just type the word 'exit' and press enter

Now to run our web-app:
	- Navigate to the root directory and install flask by using the command;
			- "pip install flask"
	- After installing run the command "python web_app/app.py "
	- The open your bowser and type http://127.0.0.1:5000