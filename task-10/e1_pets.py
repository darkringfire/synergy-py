pets = {}

in_pet_name = input("Введите имя питомца: ")
in_pet_type = input("Введите вид питомца: ")
in_pet_age = int(input("Введите возраст питомца: "))
in_owner_name = input("Введите имя владельца: ")

pets[in_pet_name] = {
    "Вид питомца": in_pet_type,
    "Возраст питомца": in_pet_age,
    "Имя владельца": in_owner_name
}


for pet_name, pet in pets.items():
    pet_type = pet["Вид питомца"]
    pet_age = pet["Возраст питомца"]
    owner_name = pet["Имя владельца"]

    if pet_age % 10 == 1 and pet_age % 100 != 11:
        age_word = "год"
    elif 2 <= pet_age % 10 <= 4 and (pet_age % 100 < 10 or pet_age % 100 >= 20):
        age_word = "года"
    else:
        age_word = "лет"

    print(f'Это {pet_type.lower()} по кличке "{pet_name}". Возраст питомца: {pet_age} {age_word}. Имя владельца: {owner_name}')
