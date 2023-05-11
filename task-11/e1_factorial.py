def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_list(f):
    result = []
    for i in range(f, 0, -1):
        result.append(factorial(i))
    return result

n = int(input('Введите число: '))
f = factorial(n)
print(f'Факториал {n} равен {f}')
print(factorial_list(f))
