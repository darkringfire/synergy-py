n = int(input("Enter the number of integers: "))

numbers = []

for i in range(n):
    number = int(input(f"Enter integer {i + 1}: "))
    numbers.append(number)

numbers.reverse()

for number in numbers:
    print(number)
