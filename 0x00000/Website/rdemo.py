import requests
r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))
print()
print(r.text)
print()
