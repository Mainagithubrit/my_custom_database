"""A simple class used to find words fast in our database
we use standard python dictionary"""

class Index:
    def __init__(self):
        """Initializing our key components"""
        # This dictionary will store Key -> Row Index Mapping
        self.lookup_map = {}

    def add_entry(self, key, position):
        """Adds a record to the Index
        key: The value of the Primary Key
        position: where that row lives in the table's list"""

        self.lookup_map[str(key)] = position

    def get_position(self, key):
        """Quickly retrieves the row position for a given key.
            Returns None if the key doesn't exist."""

        return self.lookup_map.get(str(key))

    def remove_entry(self, key):
        """Removes a key from thr index (used during DELETE)."""
        if str(key) in self.lookup_map
            del self.lookup_map[str(key)]

    def rebuild(self, rows, key_name):
