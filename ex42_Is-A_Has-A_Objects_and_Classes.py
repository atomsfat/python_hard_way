class Animal(object):
    pass


class Dog(Animal):

    def __init__(self, name):
        self.name = name


# is a
class Cat(Animal):

    def __init__(self, name):
        self.name = name


# is a object
class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None


# is a
class Employee(Person):

    def __init__(self, name, salary):
        # calling parent constructor
        super(Employee, self).__init__(name)
        # has a
        self.salary = salary


# is a
class Fish(object):
    pass


# is a
class Salmon(Fish):
    pass


# is a
class Halibut(Fish):
    pass


# rover is a dog
rover = Dog("Rover")

# Satan is a cat
satan = Cat("Satan")

# Mary is a person
mary = Person("Mary")

# Mary has cat called satan
mary.pet = satan

# Frank is a Employee
frank = Employee("Frank", 12000)

# Frank has a pet
frank.pet = rover

# Flipper is a fish
flipper = Fish()

# Crouse is a salmon
crouse = Salmon()

# Harry is a halibut
harry = Halibut()
