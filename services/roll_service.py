import json
import time

from db.db_adapter import DBAdapter


class RollService:
    def __init__(self):
        self.db = DBAdapter()

    def roll(self, data):
        print(data)
        self.db.save_roll(data)

        result = None
        repeats = 0
        while result is None:
            time.sleep(1)
            result, repeats = self.db.get_roll(data.get('author'))
        self.db.see_roll(data.get('author'))
        return json.loads(result), repeats

    def reset_table(self):
        self.db.reset_table()
