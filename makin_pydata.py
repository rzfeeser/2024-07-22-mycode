#!/usr/bin/python3

"""creating legal python data from json"""

import json

def main():
    """runtime"""
    with open("starwars.json", "r") as swj:
        swpydata = json.load(swj) # this decodes the string as a dictionary (or list)
        #swpydata = swj.read()    # this reads anything in any file as a string

    print(swpydata)
    print(type(swpydata))

main()
