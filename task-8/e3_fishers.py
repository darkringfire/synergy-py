m = int(input("Enter the maximum weight a boat can carry: "))
n = int(input("Enter the number of fishers: "))

weights = []

for i in range(n):
    weight = int(input(f"Enter the weight of fisher {i + 1}: "))
    weights.append(weight)

weights.sort()

boat_count = 0

while len(weights) > 0:
    if len(weights) == 1 or weights[0] + weights[-1] > m:
        boat_count += 1
        print("Boat {}: {}".format(boat_count, weights.pop()))
    else:
        boat_count += 1
        print("Boat {}: {}+{}".format(boat_count, weights.pop(0), weights.pop()))

print(f"The minimum number of boats needed is {boat_count}")
