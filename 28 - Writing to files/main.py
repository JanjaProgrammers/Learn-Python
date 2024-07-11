with open("test.txt", 'w') as file:
    lines = ["First line.\n", "Second line.\n", "Third line.\n"]
    file.writelines(lines)