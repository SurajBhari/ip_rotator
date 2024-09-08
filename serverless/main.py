
import json
import requests
from requests.auth import HTTPBasicAuth

with open('config.json') as f:
    config = json.load(f)

domain = config['domain']
record = config['key']
ip = requests.get('https://api.ipify.org').text

token = config['name.com.token']
username = config['name.com.username']
url = f"https://api.name.com/v4/domains/{domain}/records"
auth = HTTPBasicAuth(username, token)
response = requests.get(url, auth=auth)
if response.status_code != 200:
    exit(500)  # failed to get records for domain
record_id = None
for r in response.json()['records']:
    if 'host' not in r: continue
    if r['host'] == record:
        record_id = r['id']
        break
if record_id is None:
    exit(500)  # failed to find record for domain

url = f"https://api.name.com/v4/domains/{domain}/records/{record_id}"

parameters = {
    'type': 'A',
    'answer': ip    
}
payload = json.dumps(parameters)
response = requests.request(method="PUT", url=url, data=payload, auth=auth)

if response.status_code != 200:
    exit(500)  # failed to update record

print(f"Updated record {record} for domain {domain} to ip {ip}")
print(response.json()['answer'])
