with open("D:\\Learn-Python\\27 - Intro to File Handling\\test.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end="")