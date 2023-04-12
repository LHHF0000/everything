import requests

url=''
param={
    'q': '',
    'f': 'all'
}
proxies = { "http": None, "https": None}
response = requests.get(url, json=param, verify=False, proxies=proxies, timeout=60)
print(response.text)
