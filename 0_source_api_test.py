import requests
import yaml

# 读取配置文件
with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)

# 从配置文件中获取 URL 和 headers
url = config['url']
headers = config['headers']

# 定义请求的数据
data = {
    "model": "qwen1.5-32b-chat-int4",
    "messages": [
        { "role": "system",
          "content": "你是一名善解人意的小管家"
        },
        {
          "role": "user",
          "content": "去银川旅行怎么安排行程？"
        }
    ],
    "temperature": 0
}

# 发送 POST 请求
response = requests.post(url, headers=headers, json=data)

# 打印响应内容
print(response.status_code)
print(response.text)
