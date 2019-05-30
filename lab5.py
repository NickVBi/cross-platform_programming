def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end = "\t")
        print()
    print()


def matrix_square(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] ** 2
    return matrix


def matrix_square_odd(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 2 == 0:
                matrix[i][j] = matrix[i][j] ** 2
    return matrix


def matrix_square_less_5(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 5:
                matrix[i][j] = matrix[i][j] ** 2
    return matrix


def matrix_square_first_5_row(matrix):
    for i in range(4):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] ** 2
    return matrix



def matrix_square_odd_col(matrix):
    for i in range(len(matrix)):
        for j in range(1, len(matrix[i]), 2):
            matrix[i][j] = matrix[i][j] ** 2
    return matrix

def matrix_square_odd_row(matrix):
    for i in range(1, len(matrix), 2):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] ** 2
    return matrix

def matrix_square_sum_odd_row(matrix):
    sum_ = [sum([el for el in row if el % 2 == 0]) for row in matrix]
    # sum = [0] * len(matrix)
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         if matrix[i][j] % 2 == 0:
    #             matrix[i][j] = matrix[i][j] ** 2
    return sum_

def matrix_square_sum_odd_col(matrix):
    sum_ = [0] * len(matrix[0])
    for i in matrix:
        for j, el in enumerate(i):
            if el % 2 == 0:
                sum_[j] += el
    return sum_


def matrix_find_el(matrix, i, j):
    return matrix[i - 1][j - 1]

def matrix_square_find_row(matrix, i):
    return [el ** 2 for el in matrix[i - 1]]

def matrix_sum_find_col(matrix, j):
    sum_ = 0
    for el in matrix:
            sum_ += el[j - 1]
    return sum_

def matrix_find_and_change_el(matrix, i, j, value):
    matrix[i - 1][j - 1] = value
    return matrix



def task1():
    matrix = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2],
        [1, 3, 5, 7, 9, 7, 5, 3],
        [3, 1, 5, 3, 2, 6, 5, 7],
        [1, 7, 5, 9, 7, 3, 1, 5],
        [2, 6, 3, 5, 1, 7, 3, 2],
    ]

    print_matrix(matrix)
    print_matrix(matrix_square(matrix))

    # print_matrix(matrix_square_odd(matrix))

    # print_matrix(matrix_square_less_5(matrix))

    # print_matrix(matrix_square_first_5_row(matrix))


def task2():
    matrix = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2],
        [1, 3, 5, 7, 9, 7, 5, 3],
        [3, 1, 5, 3, 2, 6, 5, 7],
        [1, 7, 5, 9, 7, 3, 1, 5],
        [2, 6, 3, 5, 1, 7, 3, 2],
    ]

    print_matrix(matrix)
    # print_matrix(matrix_square_odd_col(matrix))

    # print_matrix(matrix_square_odd_row(matrix))

    # print(matrix_square_sum_odd_row(matrix))

    print(matrix_square_sum_odd_col(matrix))



def task3():
    matrix = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2],
        [1, 3, 5, 7, 9, 7, 5, 3],
        [3, 1, 5, 3, 2, 6, 5, 7],
        [1, 7, 5, 9, 7, 3, 1, 5],
        [2, 6, 3, 5, 1, 7, 3, 2],
    ]

    print_matrix(matrix)
    # i = int(input("write row: "))
    # j = int(input("write col: "))
    # print(matrix_find_el(matrix, i, j))

    # i = int(input("write row: "))
    # print(matrix_square_find_row(matrix, i))

    # j = int(input("write col: "))
    # print(matrix_sum_find_col(matrix, j))

    i = int(input("write row: "))
    j = int(input("write col: "))
    value = int(input("write value: "))
    print_matrix(matrix_find_and_change_el(matrix, i, j, value))


def main():

    # task1()
    # task2()
    task3()

if __name__ == "__main__":
    main()