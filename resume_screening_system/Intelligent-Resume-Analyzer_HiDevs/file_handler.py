import json
import os

class FileHandler:

    @staticmethod
    def load_json(filename):

        if not os.path.exists(filename):
            return []

        with open(filename,"r") as f:
            return json.load(f)

    @staticmethod
    def save_json(data, filename):

        with open(filename,"w") as f:
            json.dump(data,f,indent=4)