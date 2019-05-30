import os
import csv

PATH = './lab3_directory'



def from_csv(file_name):
    with open(file_name, "r", encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj, delimiter=';')

        result = [[value for value in line] for line in reader]
        for i in range(1, len(result)):
            for j in range(len(result[i]))[::2]:
                result[i][j] = int(result[i][j])
    return result


def to_csv(file_name, csv_list):
    with open(file_name, "w", encoding='utf-8', newline='') as f_obj:
        writer = csv.writer(f_obj, delimiter=';')
        for line in csv_list:
            writer.writerow(line)



def print_csv_list(csv_list, sort_by = 0):
    print("%-5s\t%-30s\t%-10s\t%-20s" % tuple(csv_list[0]))
    arr_t = csv_list[1::]
    arr_t.sort(key=lambda i: i[sort_by])
    for line in arr_t:
        print("%-5s\t%-30s\t%-10s\t%-20s" % tuple(line))
    print()

def incr_to_age(csv_list, group = ''):
    for i, line in enumerate(csv_list[1::]):
        if group == '' or group == line[3]:
            csv_list[i + 1][2] = int(csv_list[i + 1][2]) + 1


def decr_to_age(csv_list, group = ''):
    for i, line in enumerate(csv_list[1::]):
        if group == '' or group == line[3]:
            csv_list[i + 1][2] = int(csv_list[i + 1][2]) - 1


csv_file_path = PATH + "/student.csv"
csv_list = from_csv(csv_file_path)

def task1():
    print(len([name for name in os.listdir(PATH) if os.path.isfile(os.path.join(PATH, name))]))
    print()



def task2():

    print("Выведите информацию о студентах, отсортировав их по фамилии.")
    print_csv_list(csv_list, 1)

    print("Выведите информацию о студентах, отсортировав их по возрасту.")
    print_csv_list(csv_list, 2)

    print("Выведите информацию о студентах, отсортировав их по номеру группы.")
    print_csv_list(csv_list, 3)

    print("Выведите информацию о студентах, в возрасте старше 22 лет.")
    print("%-5s\t%-30s\t%-10s\t%-20s" % tuple(csv_list[0]))
    for line in csv_list[1::]:
        if line[2] > 22:
            print("%-5s\t%-30s\t%-10s\t%-20s" % tuple(line))

def task3():
    incr_to_age(csv_list)
    print_csv_list(csv_list)

    decr_to_age(csv_list)
    print_csv_list(csv_list)

    group = input("write group: ")
    incr_to_age(csv_list, group)
    print_csv_list(csv_list)

    decr_to_age(csv_list, group)
    print_csv_list(csv_list)

def task4():
    incr_to_age(csv_list)
    to_csv(csv_file_path, csv_list)
    new_list = from_csv(csv_file_path)
    print_csv_list(new_list)

    decr_to_age(new_list)
    to_csv(csv_file_path, new_list)
    new_list = from_csv(csv_file_path)
    print_csv_list(new_list)


def main():
    while (True):
        print("0 – Выход из программы")
        print("1 – Количество файлов в директории")
        print("2 – Считать из файла и вывести")
        print("3 – Сохранить в файл")
        print("4 – Отсортировать и вывести")
        print("5 – Прибавить возраст на 1")
        print("6 – Уменьшить возраст на 1")
        print("7 – Прибавить возраст на 1 в определенной группе")
        print("8 – Уменьшить возраст на 1 в определенной группе")

        n = int(input("Выберите опцию"))
        if (n == 0):
            break
        elif (n == 1):
            task1()
        elif (n == 2):
            print_csv_list(csv_list)
        elif (n == 3):
            to_csv(csv_file_path, csv_list)
        elif (n == 4):
            print("Сортировать по фамилии (1), возрасту(2), группе(3)?")
            n = int(input())
            print_csv_list(csv_list, n)
        elif (n == 5):
            incr_to_age(csv_list)
            print_csv_list(csv_list)
        elif (n == 6):
            decr_to_age(csv_list)
            print_csv_list(csv_list)
        elif (n == 7):
            group = input("write group: ")
            incr_to_age(csv_list, group)
            print_csv_list(csv_list)
        elif (n == 8):
            group = input("write group: ")
            decr_to_age(csv_list, group)
            print_csv_list(csv_list)

        if input("Вы хотите продолжить?") in ('no', 'N', '0'):
            break

if __name__ == "__main__":
    main()