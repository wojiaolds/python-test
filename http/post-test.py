import requests

url = 'http://192.168.188.188:9982/pay/QR/getSign.jlp'
body = {"type": "text", "content": "测试文本", "tag_id": "20717"}
headers = {'content-type': "application/x-www-form-urlencoded;charset=utf8"}

# print type(body)
# print type(json.dumps(body))
# 这里有个细节，如果body需要json形式的话，需要做处理
# 可以是data = json.dumps(body)
# response = requests.post(url, data=json.dumps(body), headers=headers)
# 也可以直接将data字段换成json字段，2.4.3版本之后支持
response  = requests.post( url, json = body, headers = headers)
response.encoding = 'utf-8'
# 返回信息
print(response.text)
# 返回响应头
print(response.status_code)