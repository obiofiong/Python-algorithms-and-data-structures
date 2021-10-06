import requests

url="https://developers.symphonyfintech.in/marketdata/auth/login"
keys={
     "appKey":"b1329cedc2fb6704cec753",
     "secretKey" : "Ccun120@gl",
     "source": "WebAPI"
}
ast = requests.post(url, data = keys)

# url="https://jsonplaceholder.typicode.com/posts"
# keys={
#     "title": 'foo',
#     "body": 'bar',
#     "userId": 1,
#   }
  
ast = requests.post(url, data = keys)
print(ast.text)