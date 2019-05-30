
def task1():
    x = int(input("print x: "))
    y = int(input("print y: "))

    x_2 = x * x
    xy = x * y
    xy6 = xy * 6
    numerator = x_2 - xy6
    y_2 = y * y
    y4_2 = y_2 * 4
    denominator = x_2 - y4_2
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("please write another value")
        return task1()
    print("x^2 = {}".format(x_2))
    print("x*y = {}".format(xy))
    print("6*x*y = {}".format(xy6))
    print("x^2-6*x*y = {}".format(numerator))
    print("y^2 = {}".format(y_2))
    print("4*y^2 = {}".format(y4_2))
    print("x^2-4y^2 = {}".format(denominator))
    print("(x^2-6*x*y) / (x^2-4y^2) = {}".format(result))
    print()

def task2():
    my_string = "ФИО;Возраст;Категория;Иванов;Иван;Иванович;23 года;Студент 3 курса;Петров;Семен;Игоревич;22 года;Студент 2 курса"

    #print(tuple(my_string.split(";")))
    print("%s\t\t\t\t\t\t%s\t\t%s\n%s %s %s\t%s\t\t%s\n%s %s %s\t%s\t\t%s" % tuple(my_string.split(";")))
    print()


def main():
    task1()
    task2()



if __name__ == "__main__":
    main()