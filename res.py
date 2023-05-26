import requests

status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/{5}', headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)

res = requests.post(f'https://petstore.swagger.io/v2/pet/{5}', headers={'accept': 'application/json'},
                    data={'name': 'mama2'})

print(res.status_code)
print(res.text)

res = requests.get(f'https://petstore.swagger.io/v2/pet/{5}', headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)

res = requests.delete(f'https://petstore.swagger.io/v2/pet/{2}', headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)

res = requests.put(f'https://petstore.swagger.io/v2/pet',
                   headers={'accept': 'application/json', 'Content-type': 'application/json'},
                   json={
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})

print(res.status_code)
print(res.text)
