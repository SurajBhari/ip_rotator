import requests
from json import load
import os 


if "config.json" not in os.listdir("."):
    print("config.json not found")
    exit(1)	   

with open("config.json", "r") as f:
    config = load(f)
    secret = config["secret"]
    server = config["server"]


response = requests.post(f"{server}/accept", json={"secret": secret})
print(response.text)