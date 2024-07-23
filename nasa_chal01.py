#!/usr/bin/python3

# python3 -m pip install python-dotenv
from dotenv import dotenv_values

# python3 -m pip install requests
import requests

# standard library
import argparse


## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():

    config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

    nasacreds = f'api_key={config.get("API_KEY", "")}'

    if not config.get("API_KEY"):   # check for creds in .env
        nasacreds += returncreds()   # if not, take from /home/student/nasa.creds


    # add our api_key=KEY
    uri_to_get = f'{NEOURL}{nasacreds}'

    # make a request with the request library
    if args.start_date and args.end_date:
        uri_to_get = f'{uri_to_get}&start_date={args.start_date}&end_date={args.end_date}'
    elif args.start_date:
        uri_to_get = f'{uri_to_get}&start_date={args.start_date}'
    elif args.end_date:
        print("this will not cause an error but we will not ONLY include an enddate in the lookup. See NASA API usage")

    # make a call
    neowrequest = requests.get(uri_to_get)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Control search parameters for nasa API")
    parser.add_argument('--start_date', metavar='START_DATE', type=str, help="What is the start date for your search (YYYY-MM-DD)?")
    parser.add_argument('--end_date', metavar='END_DATE', type=str, help="What is the end date for your search (YYYY-MM-DD)?")
    args = parser.parse_args()
    main()

