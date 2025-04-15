import requests

response  = requests.get('https://api.github.com/users').json()
print(response)