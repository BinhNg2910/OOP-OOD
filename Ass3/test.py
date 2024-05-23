import json
with open("input.json") as file:
    data = json.load(file)
    print(type(data[0]))