
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
	- The open your bowser and type http://127.0.0.1:50i00

Tech Stack & Libraries:
-  **Python:** Core programming language.
-  **Flask:** Used to build the web-app frontend.
-  **re (Regular Expressions):** The primary engine for parsing SQL commands.
-  **json:** Handles data persistence and storage.
-  **cmd:** Used to create the interactive shell environment.

How to Run
1. The Interactive REPL (CLI)
	Use this mode to execute SQL commands directly in your terminal.
		1. Navigate to the root directory: `cd my_custom_db`
		2. Run the REPL:
			python main_repl.py
		3. Type your SQL commands. To close the session, type `exit`.

2. The Web Dashboard
   Use this to view your database tables in a browser.
		1. Install Flask:
			pip install flask
		2. Run the web server:
			python web_app/app.py

3. 1. Open your browser and go to: http://127.0.0.1:5000

Author
- GitHub: https://github.com/Mainagithubrit
- LinkedIn: www.linkedin.com/in/francis-njoroge12