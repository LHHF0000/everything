import requests
import json

url = "http://xxxx:8932/v1/chat/completions"

payload = json.dumps({
  "model": "Qwen3-32B",
  "messages": [
    {
      "role": "user",
      "content": "你是谁？"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer bocsoftllm2025$'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)