import json

data = {
    "name":"aditya",
    "age":30,
    "city":"New York",
}

json_data = json.dumps(data)
# print(type(json_data))
print(json_data)


