import json

json_data = '{"name": "aditya", "age": 30, "city": "New York"}'

data = json.loads(json_data)
print(type(data))
print(data["name"])
print(data["age"])
print(data["city"])

