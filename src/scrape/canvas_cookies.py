import requests

s = requests.Session()

r = s.get('https://canvas.swansea.ac.uk')

print(r.cookies)
