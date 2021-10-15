import requests

url="https://xts.compositedge.com/marketdata/auth/login"
keys={
     "appKey":"b1329cedc2fb6704cec753",
     "secretKey" : "Acmf732$ZH",
     "source": "WebAPI"
}
  
ast = requests.post(url, json = keys)
print(ast.json())