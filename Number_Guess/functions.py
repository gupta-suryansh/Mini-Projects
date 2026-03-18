import json
import os

# correct file path (critical fix)
base = os.path.dirname(__file__)
file_path = os.path.join(base, "data.json")
players = []


def load(): #loading data from json file
    try:
        with open(file_path,"r") as f:
            data = json.load(f)

            #validation
            if  isinstance(data,list):
                players.extend(data)
            else:
                print("Invalid data format in JSON")
    except FileNotFoundError:
        pass

def save(): #saving data into json file
    with open(file_path,"w") as f:
        json.dump(players,f)