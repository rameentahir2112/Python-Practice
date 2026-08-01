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
print('I am %s %s. I learn %s.' %(first_name, last_name, language))

radius = 5
pi = 3.14
area_of_circle = pi * (radius ** 2)
print('The area of the circle with the radius %d is %.2f.' %(radius, area_of_circle))

python_libraries = ['Django', 'Flask', 'Numpy', 'Matplotlib', 'Pandas']
print('The following are the Python Libraries %s.' %(python_libraries))

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
last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)

# Reversing a string
language = 'Python'
print(language[::-1])

# Slicing String by Skipping a Character
language = 'Python'
print(language[0:6:2])

# String Methods

# capitalize(): Converts the first character of the string to capital letter
challenge = 'thirty days of python'
print(challenge.capitalize()) 

# count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))

# endswith(): Checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on')) # True
print(challenge.endswith('tion')) # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

# find(): Returns the index of the first occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))
print(challenge.rfind('th'))

# format(): formats string into a nicer output
first_name = 'Rameen'
last_name = 'Tahir'
age = 21
job = 'student'
country = 'Pakistan'
formatted_string = 'I am {} {}. I am {} years old. I am a {}. My country is {}.'.format(first_name, last_name, age, job, country)
print(formatted_string)

radius = 5
pi = 3.14
area_of_circle = pi * (radius ** 2)
formatted_string = ('The area of circle with radius {} is {:.2f}.'.format(radius, area_of_circle))
print(formatted_string)

# index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))

# rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))
print(challenge.rindex('on', 8))

# isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())
challenge = 'Thirty days of python'
print(challenge.isalnum())
challenge = '30DaysPython'
print(challenge.isalnum())

# isalpha(): Checks if all characters are alphabetic
challenge = 'ThityDaysPython'
print(challenge.isalpha())
challenge = 'Thirty days of python'
print(challenge.isalpha())
challenge = '30DaysPython'
print(challenge.isalpha())

# isdecimal(): Checks if all characters are decimal (0-9)
challenge = 'ThirtyDaysPython'
print(challenge.isdecimal())
challenge = '123'
print(challenge.isdecimal())
challenge = '123 4'
print(challenge.isdecimal())

# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
challenge = 'Thirty'
print(challenge.isdigit())
challenge = '\u00B2'
print(challenge.isdigit())
challenge = '30'
print(challenge.isdigit())

# isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
challenge = '10'
print(challenge.isnumeric())
challenge = '10.5'
print(challenge.isnumeric())
challenge = '\u00BD'
print(challenge.isnumeric())

# isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())

# islower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower())
challenge = 'Thirty Days Of Python'
print(challenge.islower())

# isupper(): Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper())
challenge = 'Thirty Days Of Python'
print(challenge.isupper())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())

# join(): Returns a concatenated string
web = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web)
print(result)

# strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of python'
print(challenge.strip('thon'))

# replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))

# split(): Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split())
challenge = 'thirty,days,of,python'
print(challenge.split(','))

# title(): Returns a title cased string
challenge = 'thirty days of python'
print(challenge.title())

# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'thirty days of python'
print(challenge.swapcase())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.swapcase())

# startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))
challenge = '30 days of python'
print(challenge.startswith('thirty'))

# endswith(): Checks if String Ends with the Specified String
challenge = 'thirty days of python'
print(challenge.endswith('python'))