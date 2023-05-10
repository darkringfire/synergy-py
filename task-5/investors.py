min_investment = int(input("Enter the minimum investment amount: "))
michael_money = int(input("Enter the amount of money Michael has: "))
ivan_money = int(input("Enter the amount of money Ivan has: "))

if michael_money >= min_investment and ivan_money >= min_investment:
    print(2)
elif michael_money >= min_investment:
    print("Mike")
elif ivan_money >= min_investment:
    print("Ivan")
elif michael_money + ivan_money >= min_investment:
    print(1)
else:
    print(0)
