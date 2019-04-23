cars = 100
space_in_car = 4.0
drivers = 30
passenger = 90
cars_not_driven = cars-drivers
cars_driven = drivers
car_pool_capacity = cars_driven * space_in_car
average_person_by_car = passenger / cars_driven

print("There are ", cars, " cars available")
print("There are ", drivers, " drivers available")
print("There will be ", cars_not_driven, " empty cars today")
print("We can transport ", car_pool_capacity, " people today")
print("We have ", passenger, " to car pool today")
print("We need to put about", average_person_by_car, " in each car")
