"""This module acts as a general manager.
    It manages the entire database folder, it creates new tables and
    routes SQL commands to the correct table"""

import os
import re
from engine.table import Table
from engine.parser import SQLParser

class SimpleDB:
    def __init__(self, data_dir='data'):
        self.data_dir = data_dir
        self.tables = {}
        self.parser = SQLParser()

        # Ensure the data folder exists
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

        # Automatically find and load any existing .json tables
        self.autoload_tables()

    def autoload_tables(self):
        """This function looks at the data folder and loads every table if finds"""
        for filename in os.listdir(self.data_dir):
            if filename.endswith(".json"):
                table_name = filename.replace(".json", "")
                # assuming 'id' is the primary key for simple autoload_tables
                self.tables[table_name] = Table(table_name, [], 'id')

    def create_table(self, name, columns, primary_key='id'):
        """Creates a new table and keeps track of it"""
        if name in self.tables:
            return f"Table '{name}' already exists."
        
        new_table = Table(name, columns, primary_key)
        self.tables[name] = new_table
        return f"Table '{name}' created successfully"

    def execute(self, query):
        """This uses the parser to route the Command"""

        # Logic for 'JOIN' "SELECT FROM table1 JOIN table2 ON table1.id"
        if "join" in query.lower():
            return self.handle_join(query)

        # Uses the parser for all other commands
        parsed = self.parser.parse(query)
        if not parsed:
            return "Command not recognized"

        cmd = parsed['command']
        table_name = parsed.get('table')

        if cmd == 'create':
            cols = [c.strip() for c in parsed['cols'].split(",")]
            # First column is assumed to be the Primary key
            return self.create_table(table_name, cols, cols[0])

        if table_name not in self.tables:
            return f"Error: Table '{table_name}' not found."

        table = self.tables[table_name]


        # Logic to handle SELECT
        if cmd == "select":
            return table.select(parsed.get('filter_col'), parsed.get('filter_val'))

        # Logic to handle INSERT
        if cmd == 'insert':
            values = [v.strip().strip("'") for v in parsed['values'].split(",")]
            # Maps values to columns
            row_dict = dict(zip(table.columns, values))
            return table.insert(row_dict)

        # Logic to handle DELETE
        if cmd == 'delete':
            return table.delete(parsed['filter_col'], parsed['filter_val'])

        # Logic to hadle 'update'
        if cmd == 'update':
            new_data = {parsed['set_col']: parsed['set_val'].strip("'")}
            return table.update(parsed['filter_col'], parsed['filter_val'], new_data)

        return "Command not recognized"

    def handle_join(self, query):
        """Links two tables together by comparing values"""
        # A regex that looks fro the table names and the columns to match on 

        match = re.search(r"from (\w+) join (\w+) on (\w+)\.(\w+) = (\w+)\.(\w+)", query, re.IGNORECASE)
        if not match:
            return "Join Error: User format 'FROM t1 JOIN t2 ON t1.col = t2.col'"
        
        t1_name, t2_name, _, t1_col, _, t2_col = match.groups()

        if t1_name in self.tables and t2_name in self.tables:
            data1 = self.tables[t1_name].select()
            data2 = self.tables[t2_name].select()

            combined = []

            # 'Nested Loop that compare every row of t1 to every row of T2'
            for r1 in data1:
                for r2 in data2:
                    if str(r1.get(t1_col)) == str(r2.get(t2_col)):
                        # create a new dictionary containing data from both 
                        combined.append({**r1, **r2})
            return combined
        return "Error: One or both tables not found"
