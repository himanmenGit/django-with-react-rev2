import requests

TOKEN = '450cc48d30c6d43bf94219f1ca5ccdde1c9c231'
JWT_TOKEN = 'yJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InVzZXIyIiwiZXhwIjoxNjE4MjkzODQ2LCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNjE4MjkzNTQ2fQ.BqYjh2OfIk20rENrottQOUKB62brkVmITabSHysdHM8'
headers = {
    # 'Authorization': f'Token {TOKEN}'
    'Authorization': f'JWT {JWT_TOKEN}'
}

res = requests.get("http://localhost:8000/post/1/", headers=headers)
print(res.json())
