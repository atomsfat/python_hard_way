from sys import argv

script, filename = argv

print(f"We are going to erase {filename}")
print("If you dont want that, hit CTRL-C")

print("If you want that, hit RETURN")
input("?")
print("opening file")

target = open(filename, 'w')
print("Truncating file. Goodbye !")
target.truncate()
print("now give three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Writing lines to file")
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("Finally, closing file")
target.close()
