states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
        }
cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
        }
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print('NY state has: ', cities['NY'])
print('OR state has: ', cities['OR'])

print('-' * 10)
print('Michigan abbrevation is', states['Michigan'])
print('Florida abbrevation is', states['Florida'])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} is abbreviated {abbrev}')

print('-' * 10)
for city, abbrev in list(cities.items()):
    print(f'{abbrev} has the {city}')

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} has city {cities[abbrev]}')

print('-' * 10)

state = states.get('Texas')

if not state:
    print('Sorry, no Texas')


city = cities.get('TX', 'Does not exist')
print(f'The city of \'TX\' is: {city}')
