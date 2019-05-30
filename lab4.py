import os
import csv
import operator


PATH = './lab3_directory'



def from_csv(file_name):
    with open(file_name, "r", encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj, delimiter=';')
        result = {line[0]: [int(value) if value.isnumeric() else value for value in line[1:]] for line in reader}
    return result


def to_csv(file_name, csv_dict):
    with open(file_name, "w", encoding='utf-8', newline='') as f_obj:
        writer = csv.writer(f_obj, delimiter=';')
        for key, value in csv_dict.items():
            writer.writerow([key] + value)



def print_csv_list(csv_dict, sort_by = 0):
    # arr_t = csv_dict[1::]
    # arr_t.sort(key=lambda i: i[sort_by])
    if sort_by != 0:
        sorted_x = sorted(csv_dict.items(), key=operator.itemgetter(sort_by))
        for key, value in sorted_x:
            print("%-5s\t" % key + "%-30s\t%-10s\t%-20s" % tuple(value))
        return
    for key, value in csv_dict.items():
        print("%-5s\t" % key + "%-30s\t%-10s\t%-20s" % tuple(value))
    print()

def incr_to_age(csv_dict, group = ''):
    for key, value in csv_dict.items():
        if (group == '' or group == value[2]) and key.isnumeric():
            csv_dict[key][1] = int(csv_dict[key][1]) + 1


def decr_to_age(csv_dict, group = ''):
    for key, value in csv_dict.items():
        if (group == '' or group == value[2]) and key.isnumeric():
            csv_dict[key][1] = int(csv_dict[key][1]) - 1


csv_file_path = PATH + "/student.csv"
csv_dict = from_csv(csv_file_path)

def task1():
    dictionary = {
        'марафон': 'гонка бегунов длиной около 26 миль',
        'персона': 'человек',
        'бежал': 'бежать в прошедшем времени',
        'бежать': 'двигаться со скоростью',
        'туфля': 'род обуви, закрывающей ногу не выше щиколотки',
        'туфли': 'туфля во множественном числе'
    }
    print(len(dictionary.keys()))


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
            print_csv_list(csv_dict)
        elif (n == 3):
            to_csv(csv_file_path, csv_dict)
        elif (n == 4):
            print("Сортировать по фамилии (1), возрасту(2), группе(3)?")
            n = int(input())
            print_csv_list(csv_dict, n)
        elif (n == 5):
            incr_to_age(csv_dict)
            print_csv_list(csv_dict)
        elif (n == 6):
            decr_to_age(csv_dict)
            print_csv_list(csv_dict)
        elif (n == 7):
            group = input("write group: ")
            incr_to_age(csv_dict, group)
            print_csv_list(csv_dict)
        elif (n == 8):
            group = input("write group: ")
            decr_to_age(csv_dict, group)
            print_csv_list(csv_dict)

        if input("Вы хотите продолжить?") in ('no', 'N', '0'):
            break

if __name__ == "__main__":
    main()