import random


def generate_matrix(rows, cols):
    return [[random.randint(-50, 200) for j in range(cols)] for i in range(rows)]


def add_matrices(matrix1, matrix2):
    result_matrix = []
    for i in range(len(matrix1)):
        result_row = []
        row1 = matrix1[i]
        for j in range(len(row1)):
            result_row.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(result_row)
    return result_matrix


def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(f"{item:5}", end="")
        print()


rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix_1 = generate_matrix(rows, cols)
matrix_2 = generate_matrix(rows, cols)

result_matrix = add_matrices(matrix_1, matrix_2)

print("Матрица 1:")
print_matrix(matrix_1)

print("Матрица 2:")
print_matrix(matrix_2)

print("Результирующая матрица:")

print_matrix(result_matrix)
