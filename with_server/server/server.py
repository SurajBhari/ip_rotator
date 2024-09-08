from flask import Flask, request
import json
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)



@app.route("/")
def slash():
    return "Hello, World!"


@app.route("/accept", methods=["POST"])
def accept():
    data = request.get_json()
    try:
        secret = data["secret"]
    except KeyError:
        return "No secret provided", 400
    with open("config.json", "r") as f:
        config = json.load(f)
    try:
        stored_secret = config["secret"]
    except KeyError:
        return "config.json is missing secret", 500
    
    if secret != stored_secret:
        return "Invalid secret", 403
    
    domain = config['domain']
    record = config['key']
    ip = request.remote_addr

    token = config['name.com.token']
    username = config['name.com.username']
    url = f"https://api.name.com/v4/domains/{domain}/records"
    auth = HTTPBasicAuth(username, token)
    response = requests.get(url, auth=auth)
    if response.status_code != 200:
        return f"Failed to get records for {domain}", 500
    record_id = None
    for r in response.json()['records']:
        if 'host' not in r: continue
        if r['host'] == record:
            record_id = r['id']
            break
    if record_id is None:
        return f"Failed to find record {record} for domain {domain}", 500
    
    url = f"https://api.name.com/v4/domains/{domain}/records/{record_id}"

    parameters = {
        'type': 'A',
        'answer': ip    
    }
    payload = json.dumps(parameters)
    response = requests.request(method="PUT", url=url, data=payload, auth=auth)
    
    if response.status_code != 200:
        return "Error Updating Record", 500
    return response.json()['answer']
    #return f"Accepted request for {domain} with record {record} for ip {ip}", 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)