
# import json
# # person ={"name": "John", "age": 30, "city": "New York"}

# # # Convert Python object to JSON string
# # json_string = json.dumps(person, ident =4, sort_keys=True)
# # print(personJSON)

# # with open('person.json', 'w') as file:
# #     json.dump(person,file , indent=4, sort_keys=True)

# def _init_(self,name,age):
#     self.name = name
#     self.age = age

# user = User('Max',25)

# def encode_user(o):
#     if isinstance(o, User):
#         return {'name': o.name, 'age': o.age, o._class__._name_:True}
#     else:
#         raise TypeError(f'Object of type {o.__class__.__name__} is not JSON serializable')
    
# from json import JSONEncoder
# class UserEncoder(JSONEncoder):

#     def default(self, o):
#     if isinstance(o, User):
#         return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
#     return JSONEncoder.default(self, o)
# userJSon = UserEncoder().encode(user)
# print(userJSon)
