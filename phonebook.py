from os import path

lastid = 0
file_base = "numbers.txt"
all_data = []


if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, lastid
    with open(file_base, encoding="utf-8") as numbers:
        all_data = [i for i in numbers]
        if all_data:
            lastid = int(all_data[-1].split()[0])
            return all_data
        return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Database is empty!")


def add_data():
    global lastid, all_data
    with open(file_base, "a", encoding="utf-8") as numbers:
        data = str(lastid) + " " + input()
        numbers.write(data)
        lastid += 1


def change_data(idchange):
    global all_data
    print(all_data)
    for i in range(len(all_data)):
        print(i)
        if all_data[i][0] == idchange:
            all_data[i] = idchange + " " + input()
            break


def delete_data(iddelete):
    global all_data
    for i in range(len(all_data)):
        if all_data[i][0] == iddelete:
            all_data.pop(i)
            break


read_records()
print(all_data)
change_data('0')
print(all_data)