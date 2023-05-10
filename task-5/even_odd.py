number = int(input("Введите число: "))

if number < 0:
    description = "отрицательное"
elif number == 0:
    description = "нулевое"
else:
    description = "положительное"

if number % 2 == 0:
    description += " четное"
else:
    description += " нечетное"
    print("число не является четным")

print(f"{description} число")
