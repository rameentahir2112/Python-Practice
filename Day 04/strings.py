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