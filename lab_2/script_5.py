import json

user = {
    "name": "Александр",
    "age": 25,
    "city": "Тула",
}
print(f"Словарь user: {user}")

with open("test.json", "w") as file:
    json.dump(user, file)

dict_to_object = json.dumps(user, ensure_ascii=False)
print(f"Преобразование в json: {dict_to_object}")
object_to_dict = json.loads(dict_to_object)
print(f"Преобразование из json: {object_to_dict}")

with open("test.json", "r") as file:
    data = json.load(file)
    print(f"Чтение из файла: {data}")