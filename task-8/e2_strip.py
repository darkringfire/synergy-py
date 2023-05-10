n = int(input("Enter the number of integers: "))

numbers = list(
    map(int, input("Enter the integers separated by spaces: ").split()))

last = numbers.pop()
numbers.insert(0, last)

print(*numbers)
