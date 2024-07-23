#!/usr/bin/python3
"""creating a script that outputs a json file"""

# exporing 
import json

def main():
    """runtime code"""

    python_data_blob = {"mutant_power": None, "hero": "batman", "name": "bruce wayne", "hideout": "cave", "symbol": "bat", "injury": False}

    with open("super_hero.json", "w") as shj:
        json.dump(python_data_blob, shj) # write out to the file super_hero.json


    print(json.dumps(python_data_blob)) # dump python data to legal json string





main()
