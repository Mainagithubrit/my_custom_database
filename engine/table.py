"""This is a simple table class that acts as my core storage manager.
    It checks that the data follows the rules and saves it in a .json file"""

import json
import os
from engine.index import Index

class Table:
    def __init__(self, name, columns, primary_key):
        """This is where I initialize my key components"""
        self.name = name
        self.columns = columns
        self.primary_key = primary_key
        self.rows = []
        self.file_path = f"data/{name}.json"

        self.index = Index()

        # Load existing data if the file existing
        if os.path.exists(self.file_path):
            self.load()

            self.index.rebuild(self.rows, self.primary_key)

    def insert(self, row_data):
        """This adds a new row after checking rules."""
        # 1. Primary Key Check: Ensure the ID isn't already where
        pk_value = row_data.get(self.primary_key)
        for existing_row in self.rows:
            if existing_row.get(self.primary_key) == pk_value:
                raise Exception(f"Error: Duplicate Primary Key '{pk_value}'")

        # 2. Add the data
        self.rows.append(row_data)
        new_pos = len(self.rows) - 1
        pk_value = row_data.get(self.primary_key)
        self.index.add_entry(pk_value, new_pos)

        self.save()
        return "Row inserted succesfully."
    
    def select(self, filter_col=None, filter_val=None):
        """Returns rows, optionally filtered (like a WHERE clause)."""
        if not filter_col:
            return self.rows

        return [r for r in self.rows if str(r.get(filter_col)) == str(filter_val)]

    def update(self, filter_col, filter_val, new_data):
        """Modifies existing rows.
        new_data: A dictionary of columns to change"""

        updated_count = 0

        # Loop through all rows to find matches 
        for row in self.rows:
            if str(row.get(filter_col)) == str(filter_val):
                # Updatethe row with new values
                row.update(new_data)
                updated_count +=1

        # If we updated anything, save it 
        if updated_count > 0:
            # If the Primary key was changed, we rebuild the index 
            if self.primary_key in new_data:
                self.index.rebuild(self.rows, self.primary_key)

            self.save()
        return f"Updated {updated_count} rows."

    def delete(self, filter_col, filter_val):
        """Removes rows that match the filter."""
        original_count = len(self.rows)

        if filter_col == self.primary_key:
            self.index.remove_entry(filter_val)

        self.rows = [r for r in self.rows if str(r.get(filter_col)) != str(filter_val)]

        self.index.rebuild(self.rows, self.primary_key)
        self.save()
        return f"Deleted {original_count - len(self.rows)} rows."

    def save(self):
        """This writes the current table to a JSON file."""
        with open(self.file_path, 'w') as f:
            json.dump(self.rows, f)

    def load(self):
        """Reads the table from the JSON file."""
        with open(self.file_path, 'r') as f:
            self.rows = json.load(f)
