# ex4.py  变量和命名

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers             # 70
cars_driven = drivers                         # 30
carpool_capacity = cars_driven * space_in_a_car   #120.0
average_passengers_per_car = passengers / cars_driven     # 3

print(f'There are {cars} cars available.')
print(f'There are only {drivers} drivers available. ')
print(f'There will be {cars_not_driven} empty cars today.')
print(f'We can transport {carpool_capacity} people today.')
print(f'We have {passengers} to carpool today.')
print(f'We need to put about {average_passengers_per_car} in each car.')