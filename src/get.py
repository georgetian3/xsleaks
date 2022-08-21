import requests
from time import time

start = time()
resp = requests.get('http://georgetian.com:8880/logo')

print(resp)