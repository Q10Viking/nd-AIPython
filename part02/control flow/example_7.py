# creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

print(cities)
for index in range(len(cities)):
    cities[index] = cities[index].title()
print(cities)

'''
['new york city', 'mountain view', 'chicago', 'los angeles']
['New York City', 'Mountain View', 'Chicago', 'Los Angeles']
'''