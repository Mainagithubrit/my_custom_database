"""This is class takes SQL string and break it into a python dictionary"""

import re

class SQLParser:
    def __init__(self):
        """Initializes key components
        These are Patterns for different SQL commands"""
        self.patterns = {
            'select' : r"select\s+(?P<cols>.+)\s+from\s+(?P<table>\w+)(?:\s+where\s+(?P<filter_col>\w+)\s*=\s*(?P<filter_val>.+))?",
            'insert' : r"insert\s+into\s+(?P<table>\w+)\s+values\s*\((?P<values>.+)\)",
            'create' : r"create\s+table\s+(?P<table>\w+)\s*\((?P<cols>.+)\)",
            'delete' : r"delete\s+from\s+(?P<table>\w+)\s+where\s+(?P<filter_col>\w+)\s*=\s*(?P<filter_val>.+)",
            'update' : r"update\s+(?P<table>\w+)\s+set\s+(?P<set_col>\w+)\s*=\s*(?P<set_val>.+)\s+where\s+(?P<filter_col>\w+)\s*=\s*(?P<filter_val>.+)"
        }

    def parse(self, query):
        """Identifies the command type and extracts key data."""
        query = query.strip()

        for command, pattern in self.patterns.items():
            match = re.match(pattern, query, re.IGNORECASE)
            if match:
                # Returns a dictionary of the matched groups
                result = match.groupdict()
                result['command'] = command
                return result

        return None
