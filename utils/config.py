import json

def load(config_path):
    with open(config_path, "r") as file:
        return json.load(file)
