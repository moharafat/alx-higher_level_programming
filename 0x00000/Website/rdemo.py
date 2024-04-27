import requests
r = requests.get('https://httpbin.org/basic-auth/corey/testing', timeout=3)
print()
print(r)
print()
