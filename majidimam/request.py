import requests

r = requests.get('http://www.google.com')
print("Response Status", r.status_code)

print(r.text)
