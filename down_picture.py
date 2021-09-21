import requests as req

url = 'https://news.xfastest.com/wp-content/uploads/2021/08/applestoredown.jpg'
r = req.get(url)

with open('123.jpg', mode='wb') as file:
    file.write(r.content)

#print(r.content)
