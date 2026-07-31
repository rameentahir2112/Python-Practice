# Creating String

letter = 'R'
print(letter)
print(len(letter))
greeting = 'Hello World!'
print(greeting)
print(len(greeting))
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

first_name = 'Rameen'
last_name = 'Tahir'
full_name = first_name + last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

print('I am enjoying the 30 days Python challenge. \nAre you?')
print('Days\tTopic\tExercises')
print('Day 01\t1\t3')
print('Day 02\t2\t5')
print('Day 03\t3\t6')
print('This is a backslash symbol(\\)')
print('Every programming language starts with \"Hello World\"')

first_name = 'Rameen'
last_name = 'Tahir'
language = 'Python'
print('I am %s %s. I learn %s.')%(first_name, last_name, language)

radius = 5
pi = 3.14
area_of_circle = pi * (radius ** 2)
print('The area of the circle with the radius %d is %.2f.')%(radius, area_of_circle)

python_libraries = ['Django', 'Flask', 'Numpy', 'Matplotlib', 'Pandas']
print('The following are the Python Libraries %s.')%(python_libraries)

first_name = 'Rameen'
last_name = 'Tahir'
language = 'Python'
formatted_string = 'I am {} {}. I learn {}.'.format(first_name, last_name, language)
print(formatted_string)

a = 10 
b = 5

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

radius = 10
pi = 3.14
area_of_circle = pi * (radius ** 2)
formatted_string = ('The area of circle with radius {} is {:.2f}.'.format(radius, area_of_circle))
print(formatted_string)

a = 5
b = 4

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

language = 'Python'
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Accessing characters in String by Index
language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_letter = language[len(language) - 1]
print(last_letter)
last_index = len(language) - 1
print(last_index)

# If we want to access the string from last, we can start it from -1.
language = 'Python' 
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)

# Slicing Python String
language = 'Python'
first_three = language[0:3] # Starts at zero index and up to index 3 but not include index 3
print(first_three)
last_three = language[3:6]
print(last_three)
# Another way

