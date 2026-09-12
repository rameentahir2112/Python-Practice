# Exercise

# Level 1

# Task 1: Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive.')
else:
    years_left = 18 - age
    print(f'You are not old enough to drive. You need to wait {years_left} more years.')

# Task 2:Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 25
your_age = int(input('Enter your age: '))
if my_age > your_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print('You are 1 year younger than me.')
    else:
        print(f'You are {age_difference} years younger than me.')
elif my_age < your_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print('You are 1 year older than me.')
    else:
        print(f'You are {age_difference} years older than me.')
else:
    print('We are the same age.')

# Task 3: Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
if a > b:
    print('a is greater than b')
elif a < b:
    print('b is greater than a')
else:
    print('a and b are equal')

# Level 2:

# Task 1: Write a code which gives grade to students according to theirs scores:
marks = int(input('Enter your marks: '))
if 90 <= marks <= 100:
    print('A')
elif 80 <= marks <= 89:
    print('B')
elif 70 <= marks <= 79:
    print('C')
elif 60 <= marks <= 69:
    print('D')
elif 0 <= marks <= 59:
    print('F')
else:
    print('Wrong input')

# Task 2: Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input('Enter a month: ')
if month == 'September' or month == 'October' or month == 'November':
    print('The season is Autumn.')
elif month == 'December' or month == 'January' or month == 'February':
    print('The season is Winter.') 
elif month == 'March' or month == 'April' or month == 'May':
    print('The season is Spring.')
elif month == 'June' or month == 'July' or month == 'August':
    print('The season is Summer.')
else:
    print('Wrong month name')

# Task 3: The following list contains some fruits: If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ')
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print('Modified list:', fruits)

# Level 3: Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    middle_skill = skills[middle_index]
    print('Middle skill:', middle_skill)
else:
    print('Key does not exist')
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print('The person has Python skill.')
else:
    print('The person does not has Python skill.')
# If a person skills has only JavaScript and React, print('He is a front end developer'). If the person skills has Node, Python, MongoDB, print('He is a backend developer'), If the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title').
if 'skills' in person:
    skills = person['skills']
    if skills == ['JavaScript', 'React']:
        print('He is a front end developer')
    elif skills == ['Node', 'Python', 'MongoDB']:
        print('He is a backend developer')
    elif skills == ['React', 'Node', 'MongoDB']:
        print('He is a fullstack developer')
    else:
        print('unknown title')