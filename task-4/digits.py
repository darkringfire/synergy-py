number = int(input("Enter a five-digit number: "))

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
ten_thousands = (number // 10000) % 10

result = (tens ** ones) * hundreds / (ten_thousands - thousands)

print(f"The result is {result}")
