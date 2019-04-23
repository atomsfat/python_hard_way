from sys import argv

script, file_input = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(file_input)


print("First print the whole file")
print_all(current_file)

print("Now rewind the file")
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
