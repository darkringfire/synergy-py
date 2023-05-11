import collections

pets = {
  1: {
    "Мухтар": {
      "Вид питомца": "Собака",
      "Возраст питомца": 9,
      "Имя владельца": "Павел"
    },
  },
  2: {
    "Каа": {
      "Вид питомца": "желторотый питон",
      "Возраст питомца": 19,
      "Имя владельца": "Саша"
    },
  }
}

def get_pet(id):
    return pets[id] if id in pets.keys() else False

def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
        return 'года'
    else:
        return 'лет'

def pets_list():
    for id in pets:
        pet = get_pet(id)
        name = list(pet.keys())[0]
        info = pet[name]
        type = info["Вид питомца"]
        age = info["Возраст питомца"]
        owner = info["Имя владельца"]
        print(f'ID: {id}. Это {type} по кличке "{name}". Возраст питомца: {age} {get_suffix(age)}. Имя владельца: {owner}')

def create(name, pet_type, age, owner):
  last = collections.deque(pets, maxlen=1)[0]
  id = last + 1
  pets[id] = {name: {"Вид питомца": pet_type, "Возраст питомца": age, "Имя владельца": owner}}

def read(id):
  pet = get_pet(id)
  if pet:
    name = list(pet.keys())[0]
    info = pet[name]
    age = info["Возраст питомца"]
    owner = info["Имя владельца"]
    type = info["Вид питомца"]
    print(f'Это {type} по кличке "{name}". Возраст питомца: {age} {get_suffix(age)}. Имя владельца: {owner}')
    return True
  print(f'Ошибка! ID={id} отсутствует в базе')
  return False

def update(id, name=None, type=None, age=None, owner=None):
  pet = get_pet(id)
  if pet:
    name = list(pet.keys())[0]
    if name is not None:
      pet = {name: pet[name]}
      name = name
    if type is not None:
      pet[name]["Вид питомца"] = type
    if age is not None:
      pet[name]["Возраст питомца"] = age
    if owner is not None:
      pet[name]["Имя владельца"] = owner

    pets[id] = pet
    return True
  print(f'Ошибка! ID={id} отсутствует в базе')
  return False

def delete(id):
  if id in pets:
    del pets[id]
    return True
  print(f'Ошибка! ID={id} отсутствует в базе')
  return False

command = ''
while command != 'stop':
  command = input('Введите команду (create/read/update/delete/stop): ')
  if command == 'create':
    name = input('Введите имя питомца: ')
    type = input('Введите вид питомца: ')
    age = int(input('Введите возраст питомца: '))
    owner = input('Введите имя владельца: ')
    create(name, type, age, owner)
  elif command == 'read':
    id = int(input('Введите идентификатор питомца: '))
    read(id)
  elif command == 'update':
    id = int(input('Введите идентификатор питомца: '))
    if read(id):
      name = input('Введите новое имя питомца (оставьте пустым, если не хотите менять): ')
      name = name if name else None
      type = input('Введите новый вид питомца (оставьте пустым, если не хотите менять): ')
      type = type if type else None
      age = input('Введите новый возраст питомца (оставьте пустым, если не хотите менять): ')
      age = int(age) if age else None
      owner = input('Введите новое имя владельца (оставьте пустым, если не хотите менять): ')
      owner = owner if owner else None
      update(id, name, type, age, owner)
  elif command == 'delete':
    id = int(input('Введите идентификатор питомца: '))
    delete(id)
  elif command == 'stop':
     break
  else:
     print("Неизвестная команда")
