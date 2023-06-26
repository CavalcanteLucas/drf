import requests

endpoint = 'http://localhost:8000/api/products/111746871/'

get_response = requests.get(
    endpoint,
)

print(get_response.text)
