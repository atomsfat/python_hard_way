import sys
script, index = sys.argv
numbers = []


def fillSome(index):
    i = 0
    while i < index:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num, type(num))

    for i in range(1, 6):
        print("Wee ", numbers.index(i), i)


fillSome(int(index))
