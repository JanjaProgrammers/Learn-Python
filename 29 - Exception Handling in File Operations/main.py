try:
    file = open("test.txt", 'r')
    print(file.read())
except FileNotFoundError:
    print("The file does not exist")

print("Working fine")