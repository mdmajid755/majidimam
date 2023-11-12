import requests
from io import BytesIO
from PIL import Image 

r = requests.get('http://www.google.com')
print("Response Status", r.status_code)

print(r.text)

with open('./page1.html', 'w+') as f:
    f.write(r.text)

requestParams = {"q":"pizza"}
try:
    r = requests.get('http://www.google.com', params=requestParams)
    print(r.url)
    print("Response Status", r.status_code)
    # print(r.text)

    with open('./googlePizzaPage.html', 'w+') as f:
        f.write(r.text)
except requests.ConnectTimeout:
    print('issue with connection to google')


try:
    r = requests.get('https://search.yahoo.com/search', params=requestParams)
    print(r.url)
    print("Response Status", r.status_code)

    with open('./yahooPizzaPage.html', 'w+', encoding='utf-8') as f:
        f.write(r.text)
except requests.ConnectTimeout:
    print('issue with connection to yahoo')


r = requests.get('https://s3.amazonaws.com/photos.niche.com/11709dd5c7485cf01dc85b80dffea233a53c8086')
print(r.url)
print("Response Status", r.status_code)

image= Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)

imgPath = "./image." + image.format

try:
    image.save(imgPath, image.format)
except IOError:
    print("can not save image") 

r = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(r.status_code)
print(r.text)

r = requests.get('https://api.github.com/events')
print (r.json())