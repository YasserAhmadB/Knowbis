import requests

endpoint = 'http://127.0.0.1:8000/auth/o/google-oauth2/'
request_body = {'redirect_uri': 'http://127.0.0.1:8000/accounts/google/login/callback/',
                'state': 'mhjhkjkhkjh.kkh.iu.uih.ujhiukgjhgkyfiduyyq;ouoeadlisawd'
                }

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
response = requests.post(endpoint, headers=headers)
print(response.content)
