N = int(input("Enter the number of integers: "))

zero_count = 0

for i in range(N):
    number = int(input(f"Enter integer {i + 1}: "))
    if number == 0:
        zero_count += 1

print(f"There are {zero_count} zeros")
