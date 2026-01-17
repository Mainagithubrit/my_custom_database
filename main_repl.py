"""This represents a simple REPL"""

from engine.database import SimpleDB
import json

def start_repl():
    """This Initializes the database"""

    db = SimpleDB(data_dir="data")

    print("--- My Custom Python RDBMS ---")
    print("Type SQL commands or 'exit' to quit.")
    print('Example: CREATE TABLE users (id, name)')

    while True:
        try:
            # READ: Get input from user 
            query = input('\nSQL> ').strip()

            if query.lower() in ['exit', 'quit']:
                print('Goodbye!')
                break

            if not query:
                continue

            # EVAL: Run the query through the database engine
            result = db.execute(query)

            # PRINT: Display the result formatted nicely
            if isinstance(result, list):
                if len(result) == 0:
                    print('Empty set (0 rows).')
                else:
                    # Print as a formatted JSON string for readability
                    print(json.dumps(result, indent=4))
            
            else:
                # Print status messages
                print(result)

        except Exception as e:
            print(f'Runtime Error: {e}')

if __name__ == "__main__":
    start_repl()
