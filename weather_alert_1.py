
# Code to alert on specific locations and send to email or SMS
# Based currently on openweathermap.org API

import requests
from os.path import exists
import pandas as pd
from io import StringIO

# CONSTANTS
API_KEY = "d7794bbe3d41d7dbcd0c93c331d5e819" # Name: weatheralert
TEST_FILE_JSON = "owmtest.json"

# METHODS

def json_to_dataframe(json_file):
    # df = pd.read_json(json_file)

    import json
    # load data using Python JSON module
    with open(json_file, 'r') as f:
        data = json.loads(f.read())
    # Flatten data
    # df = pd.json_normalize(data, record_path=['students'])
    df = pd.json_normalize(data)

    # print(df.to_string())
    return df

def dataframe_from_obj(obj): # create df from dict object
    # df = pd.DataFrame.from_dict(data)
    df = pd.DataFrame.from_dict(obj, orient="index").T
    return df

def file_exists(filename):
    file_exists = exists(filename)
    return file_exists

def file_save(file_name, content):
    f = open(file_name, "w")
    f.write(content)
    print(".... request content saved to file: " + file_name)
    f.close()

# https://api.openweathermap.org/data/3.0/
# onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}
url = "https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=" + API_KEY
print(url)

url = "https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid=" + API_KEY
print(url)

# check if test file exists and use if true, if not make request from API
if file_exists(TEST_FILE_JSON) == False:
    r = requests.get(url)
    print(r)
    df = dataframe_from_obj(r.json())  # get df from request object
    file_save(TEST_FILE_JSON, r.text)  # use this file to test code without having to perform request
else: #read the test file and retrieve content, to dataframe?
    df = json_to_dataframe(TEST_FILE_JSON)


print (df)











