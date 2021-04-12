import requests

TOKEN = '450cc48d30c6d43bf94219f1ca5ccdde1c9c231'
headers = {
    'Authorization': f'Token {TOKEN}'
}

res = requests.get("http://localhost:8000/post/1/", headers=headers)
print(res.json())
