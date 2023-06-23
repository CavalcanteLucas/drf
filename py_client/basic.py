import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, data={"query": "Hello World"})
print(get_response.json())
print(get_response.status_code)