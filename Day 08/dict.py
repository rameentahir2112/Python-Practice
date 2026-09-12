# Creating a Dictionary

# use {} or built-in dict() function to create a dictionary
# Dictionary is a collection of key-value pairs

empty_dct = {}
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3', 'key4' : 'value4'}
person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age' : 30,
    'country' : 'USA',
    'is_married' : False,
    'skills' : ['JavaScript', 'Python', 'C++'],
    'address' : {
        'street' : '123 street',
        'city' : 'New York',
    }
}

# Dictionary Length
print('Length of dct dictionary:', len(dct))
print('Length of person dictionary:', len(person))

# Accessing Items in a Dictionary

# Accessing items using keys
print('Key 1 value in dct:', dct['key1'])
print('Key 4 value in dct:', dct['key4'])

print('First name:', person['first_name'])
print('Last name:', person['last_name'])
print('Age:', person['age'])
print('Country:', person['country'])
print('Is married:', person['is_married'])
print('Skills:', person['skills'])
print('First skill:', person['skills'][0])
print('Street:', person['address']['street'])
print('Address:', person['address'])
# print('City:', person['city']) will throw an error

# Using get method
print('First name:', person.get('first_name'))
print('Last name:', person.get('last_name'))
print('Country:', person.get('country'))
print('Skills:', person.get('skills'))
print('First skill:', person.get('skills')[0])
print('Street:', person.get('address').get('street'))
print('Address:', person.get('address'))
print('City:', person.get('address').get('city')) # will return None

# Adding Items to a Dictionary
# Adding a new key-value pair to the dictionary
dct['key5'] = 'value5'
person['job_title'] = 'Engineer'
person['skills'].append('HTML')
print(dct)
print(person)

# Modifying Items in a Dictionary
# Modifying an existing key-value pair in the dictionary
dct['key1'] = 'value-one'
person['first_name'] = 'alice'
person['age'] = 31
print(dct)
print(person)

# Checking Keys in a Dictionary
print('Is key1 in dct?', 'key1' in dct)
print('is key5 in dct?', 'key5' in dct)

# Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name
# popitem(): removes the last item
# del: removes an item with specified key name
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3', 'key4' : 'value4'}
dct.pop('key1')
print(dct)
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem()
print(dct)
del dct['key2']
print(dct)

person.pop('first_name')
person.popitem()
del person['is_married']
print(person)

# Changing Dictionary to a List of Items
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
items = dct.items()
print(items)

# Clearing a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear())

# Deleting a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

# Copy a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
print('Copy of dct:', dct_copy)

# Changing Dictionary to a List of Keys
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)

# Changing Dictionary to a List of Values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)