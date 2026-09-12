# Task 1: Create an empty dictionary called dog
dog = {}

# Task 2: Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 3

# Task 3: Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'gender' : 'male',
    'age' : 20,
    'marital_status' : 'single',
    'skills' : ['Pyhton', 'C++', 'R'],
    'country' : 'USA', 
    'city' : 'New York',
    'address' : {
        'street' : '123 street',
        'zipcode' : '1001'
    }
}

# Task 4: Get the length of the student dictionary
print('Length of student dictionary:', len(student))

# Task 5: Get the value of skills and check the data type, it should be a list
print('Skills:', student.get('skills'))
print('Data type of skills:', type(student['skills']))

# Task 6: Modify the skills values by adding one or two skills
student['skills'].append('HTML')

# Task 7: Get the dictionary keys as a list
print('Keys of student dictionary:', student.keys())

# Task 8: Get the dictionary values as a list
print('Values of student dictionary:', student.values())

# Task 9: Change the dictionary to a list of tuples using items() method
print('Student dictionary as tuples:', student.items())

# Task 10: Delete one of the items in the dictionary
del dog['name']
print('Dog:', dog)

# Task 11: Delete one of the dictionaries
del dog