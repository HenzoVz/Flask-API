import requests

# URL
url = 'http://localhost:5000/api'

# Change the value of experience that you want to test
r = requests.post(url, json={'s_length': 1.8, 's_width': 1.0, 'p_length': 2.0, 'p_width': 1.0})
print(r.json()) 