import requests
 
 
endpoint = 'http://127.0.0.1:9000/api'
response = requests.get(endpoint, data = {'query':'hello'})
print(response.json())
print(response.status_code)