import json

user = {
  "name": "Александр",
  "age": 25,
  "city": "Тула",
}
print(user)
dict_to_object = json.dumps(user, ensure_ascii=False)
print(dict_to_object)
object_to_dict = json.loads(dict_to_object)
print(object_to_dict)