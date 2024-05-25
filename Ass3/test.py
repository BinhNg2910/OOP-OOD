import json

# Sample data
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'skills': ['Python', 'Data Science']
}

# Serialization: Convert Python object to JSON string
with open("data.json", "w") as json_file:
    json.dump(data, json_file)
print("Serialized JSON string:")


# Deserialization: Convert JSON string back to Python object
with open("data.json", "r") as json_file:
    data_from_json = json.load(json_file)
print("\nDeserialized Python object:")
print(data_from_json)
