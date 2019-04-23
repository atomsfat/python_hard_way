ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that")

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now")

print("There we go: ", stuff)
print("Let's do some thing wiht stuff")

print(stuff[1])
print(stuff[-1]) # Get latest
print(stuff.pop()) # Remove latest
print(' '.join(stuff)) # Join list by space
print('#'.join(stuff[3:5])) # Join list in a range
print(pop(stuff)) # Join list in a range
