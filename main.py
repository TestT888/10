import json


with open ("data.json", 'r') as file:
    data = json.load(file)
    data.append(
        {
            "name": "Gojko",
            "age": 40,
            "height": 187,
            "gender": "male"
        }
    )
print(data)

with open("data.json", 'w') as file:
    json.dump(data, file, indent=4)
