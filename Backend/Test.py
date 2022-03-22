import requests

url = 'http://192.168.1.2:8000/platform/categories/'
myobj = {"title": "testing post"}

x = requests.post(url, data=myobj)

print(x.text)

