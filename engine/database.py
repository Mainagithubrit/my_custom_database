"""This module acts as a general manager.
    It manages the entire database folder, it creates new tables and
    routes SQL commands to the correct table"""

import os
import re
from engine.table import Table

class SimpleDB:
    def __init__(self, data_dir='data'):
        self.data_dir = data_dir
        self.tables = {}

    # Ensure the data folder exists
    if not os.path.exists(self.data_dir):
        os.makedirs(self.data_dir)

    # Automatically find and load any existing .json tables
