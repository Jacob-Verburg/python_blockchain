#1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.

persons = [
    {'name':'Jacob', 'age': 123, 'hobbies':'python'},
    {'name':'Bob', 'age': 456, 'hobbies':'games'},
    {'name':'Cheeseburger', 'age': 789, 'hobbies':'eating'}
    ]
print(persons)
#2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
names = [p['name'] for p in persons]
print(names)
#3) Use a list comprehension to check whether all persons are older than 20.
over_20 = all([p['age'] > 20 for p in persons])
print(over_20)
#4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
copied_persons = [dict(p) for p in persons]
copied_persons[0]['name'] = 'changed'
print(copied_persons)
print(persons)
#5) Unpack the persons of the original list into different variables and output these variables.
a, b, c = persons
print(a)
print(b)
print(c)
