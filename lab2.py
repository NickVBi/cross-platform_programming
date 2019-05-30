
def task1():
    arrray_string = [
        "Lorem ipsum dolor sit amet",
        "consectetur adipiscing elit,",
        "k sed do eiusmok",
        "tempor incididunt ut labore et dolore magna aliqua.",
        "Ut enim ad minim veniam",
        "k quis nostrud",
        "Excepteur",
        "sint occaecat",
        "cupidatat non proidentk",
        "sunt in culpa qui officia deserunt mollit anim id est laborum."
    ]
    print("Выведите построчно все строки размером от 9 до 17 символов.")
    for str in arrray_string:
        if 9 <= len(str) <= 17:
            print(str)
    print()

    print("Выведите построчно все строки размером менее 10 символов.")
    for str in arrray_string:
        if len(str) < 10:
            print(str)
    print()


    print("Выведите все строки, заканчивающиеся буковой k.")
    for str in arrray_string:
        if str.endswith("k"):
            print(str)
    print()

    print("Выведите все строки, начинающиеся с буквы k.")
    for str in arrray_string:
        if str.startswith("k"):
            print(str)


    print()



def task2():
    array_new = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(array_new)

    print("Удалите первые 2 элемента и добавьте 2 новых. Выведите список на экран.")
    del array_new[:2]
    array_new.extend([11, 12])
    print(array_new)

    print("Удалите все четные элементы и добавьте 2 новых. Выведите список на экран.")
    # for i in range(1, int(len(array_new) / 2) + 1):
    #     del array_new[i]
    del array_new[1::2]
    array_new.extend([13, 14])
    print(array_new)

    print("Удалите элементы с 4 по 8 и добавьте 2 новых. Выведите список на экран.")
    del array_new[3:8]
    array_new.extend([15, 16])
    print(array_new)

    print("Добавьте 5 новых элементов и оставьте все нечетные элементы. Выведите список на экран.")
    array_new.extend([17, 18, 19, 20, 21])
    del array_new[1::2]
    print(array_new)

    print()


def task3():
    n = int(input("print n: "))

    matrix = [[j * 10 + i for j in range(1, n + 1)] for i in range(1, n + 1)]

    for row in matrix:
        for el in row:
            print(el, end="\t")
        print()
    print("sum = {}".format(sum([sum([el for el in row]) for row in matrix])))
    print()




def task4():
    my_len = [
        [
            'БО - 331101',
             [
                 'Акулова Алена',
                 'Бабушкина Ксения',
                 'Рамон Растельников']
             ],
        [
            'БОВ - 421102',
            [
                'Грибон Естов',
                'Мисальна Ворова',
                'Еумик Дромон'
            ]
        ],
        [
            'БО - 331103',
            [
                'Фараон Миндельс',
                'Скандинав Тротов',
                'Торкич Гомонов'
            ]
        ]
    ]
    group_seacrh = input('write group: ')

    print("Выведите список студентов конкретной группы построчно.")
    for group in my_len:
        if group_seacrh in group:
            print(group[0])
            for person in group[1]:
                print(person)
            break
    else:
        print("group not found")

    print("Выведите список студентов конкретной группы в одной строке.")
    for group in my_len:
        if group_seacrh in group:
            print(group[0], end =":")
            for person in group[1]:
                print(person, end=",")
            print()
            break
    else:
        print("group not found")

    print("Выведите списки всех групп построчно.")
    for group in my_len:
        print(group[0])
        for person in group[1]:
            print(person)
        print()

    print("Выведите списки студентов, название группы которых начинается на «БО».")
    for group in my_len:
        if group[0].startswith("БО"):
            print(group[0], end =":")
            for person in group[1]:
                print(person, end=",")
            print()

    print("Выведите всех студентов (и их группы), если фамилия студента начинается на букву А.")
    for group in my_len:
        for person in group[1]:
            if person.startswith("А"):
                print(group[0] + ":" + person)

    print("Выведите всех студентов (и их группы), чья фамилия меньше 7 букв.")
    for group in my_len:
        for person in group[1]:
            if len(person.split(' ')[0]) < 7:
                print(group[0] + ":" + person)

    print("Выведите всех студентов (и их группы), чья фамилия начинается на букву «П», а имя на букву «А».")
    for group in my_len:
        for person in group[1]:
            person_last_name, person_first_name = person.split(' ')
            if person_last_name.startswith('П') and person_first_name.startswith('А'):
                print(group[0] + ":" + person)


    print("Выведите всех студентов (и их группы), чей порядковый номер в журнале – четное число.")
    for group in my_len:
        print(group[0], end =":")
        for person in group[1][1::2]:
            print(person)

    print()


def main():
    #task1()
    #task2()
    #task3()
    task4()



if __name__ == "__main__":
    main()