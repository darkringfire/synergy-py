X = int(input("Enter a natural number: "))

divisor_count = 0

for i in range(1, int(X ** 0.5) + 1):
    if X % i == 0:
        divisor_count += 2
        if i * i == X:
            divisor_count -= 1

print(f"There are {divisor_count} divisors")
