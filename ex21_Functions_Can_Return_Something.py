def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def substract(a, b):
    print(f"Substracting {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"Multiply {a} * {b}")
    return a * b


def divide(a, b):
    print(f"Divide {a} / {b}")
    return a / b


print("Let's do some math")
age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
print("Here is a puzzle")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))
print(f"That becomes: what ? {what} can you do by hand")
what2 = age + (height - (weight * (iq / 2)))
print(f"What 2 {what2}")
