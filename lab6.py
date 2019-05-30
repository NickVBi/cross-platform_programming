import re

def task1():
    arr_str = [
        "good (excellent) phrase",
        "good (too bad) phrase",
        "good ((recursive)) phrase"
        "word () is not () in brackets",
        "bad (() recursive) phrase",
        "no brackets here"
    ]
    str_full = ""
    with open("./lab3_directory/1.txt") as file_obj:
        for line in file_obj:
            str_full += line

    pattern = r"[\w\s]*\(+[\w\s]+[\)+)\w\s]*."
    print(re.findall(pattern, str_full))

def task2():
    str_full = ""
    with open("./lab3_directory/2.txt") as file_obj:
        for line in file_obj:
            str_full += line

    pattern = r"\((.[^\)]*)\)"
    print(re.sub(pattern, "()", str_full))

def task3():
    str_full = ""
    with open("./lab3_directory/index.html", encoding='utf-8') as file_obj:
        for line in file_obj:
            str_full += line
    res = []

    pattern = r"<a ?.* ?href=[\"']((https?:\/\/|ftp:\/\/|)([\w.-]*)[\w\/.:=?&]*)((https?:\/\/|ftp:\/\/|)([\w.-]*)[\w\/.:=?]*)?[\"'] ?.* ?>"
    t = re.findall(pattern, str_full)
    for i in t:
        if i[2] == "..":
            continue
        if i[2] not in res:
            res.append(i[2])

    for i in sorted(res):
        print(i)


def main():

    # task1()
    # task2()
    task3()

if __name__ == "__main__":
    main()