def main():
    with open("data.txt") as file:
        string_data = [line.lower().strip() for line in file]
    string_data.sort()
    for string in string_data:
        print(string)
main()


