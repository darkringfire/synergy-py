A = int(input("Enter the lower bound: "))
B = int(input("Enter the upper bound: "))

if A % 2 == 1:
    A += 1

for i in range(A, B + 1, 2):
    print(i, end=" ")
