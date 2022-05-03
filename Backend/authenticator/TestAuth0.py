import requests
url = 'https://dev-yw768gnr.us.auth0.com/authorize?'
data = {
    'response_type': 'token',
    'client_id': 'OG9L0zaI9TGTzro7U1QnpM7epjAIXeKf',
    'connection': 'github',
    'redirect_uri': 'http://192.168.1.2:8000/platform/',
}
x = requests.get(url=url, params=data)
print(x)
