
import json
person ={"name": "John", "age": 30, "city": "New York"}

# Convert Python object to JSON string
json_string = json.dumps(person, ident =4, sort_keys=True)
print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person,file , indent=4, sort_keys=True)