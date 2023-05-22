from os import path

lastid = 0
file_base = "numbers.txt"
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def validate_data(data):
    data = data.split()
    if len(data) != 4 or not data[0].isalpha() or not data[1].isalpha() or not data[2].isalpha() or not data[
        3].isnumeric():
        return False
    return True


def read_records(filepath=file_base):
    global all_data, lastid
    with open(filepath, encoding="utf-8") as numbers:
        all_data = [i for i in numbers]
        if all_data:
            lastid = int(all_data[-1].split()[0]) + 1
            return all_data
        return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Database is empty!")


def add_data():
    global lastid, all_data
    data = input()
    while not validate_data(data):
        print("Data is invalid. Please try again.")
        data = input()
    all_data.append(str(lastid) + " " + data + "\n")
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


def search_data(keyword):
    for datum in all_data:
        if keyword in datum:
            print(datum, end="")


def write_data():
    with open(file_base, "w", encoding="utf-8") as numbers:
        numbers.write("".join(all_data))


def export_data(exportfilepath):
    with open(exportfilepath, "w", encoding="utf-8") as new_file:
        new_file.write("".join(all_data))


def import_data():
    global all_data, lastid
    all_data = []
    lastid = 0
    for i in range(int(input("Enter number of entries: "))):
        all_data.append(str(lastid) + " " + input("Enter " + str(i) + "th entry") + "\n")
        lastid += 1


def menu():
    isworking = True
    read_records()
    while isworking:
        action = input('''Enter a command:\nShow all entries - p,\nAdd an entry - a\nSearch an entry - s\nEdit an entry - e\nDelete an entry - d\nExport data - x\nImport data - i\nQuit - q\n''')
        if action == "p":
            show_all()
        elif action == "a":
            add_data()
        elif action == "s":
            search_data(input())
        elif action == "e":
            show_all()
            change_data(input("Which entry (by index shown) would you like to edit?: "))
        elif action == "d":
            show_all()
            delete_data(input("Which entry (by index shown) would you like to delete?: "))
        elif action == "x":
            export_data(input("Please enter the file name (with extension) into which you would like to export: "))
        elif action == "i":
            action = input("Would you like to import from file or type in the data? (f/t): ")
            if action == "f":
                read_records(input("Enter the filepath (including file extension)"))
            elif action == "t":
                import_data()
            else:
                print("Invalid action. Try again.")
        elif action == "q":
            isworking = False
        else:
            print("Invalid action. Try again.")


if __name__ == "__main__":
    menu()
