# Exercise

# Task 1: Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
s1 = 'Thirty'
s2 = 'Days'
s3 = 'Of'
s4 = 'Python'
result = s1 + ' ' + s2 + ' ' + s3 + ' ' + s4

# Task 2: Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
s1 = 'Coding'
s2 = 'For'
s3 = 'All'
result = s1 + ' ' + s2 + ' ' + s3

# Task 3: Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# Task 4: Print the variable company using print().
print(company)

# Task 5: Print the length of the company string using len() method and print().
print(len(company))

# Task 6: Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Task 7: Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Task 8: Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company = 'Coding for all'
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Task 9: Cut(slice) out the first word of Coding For All string.
company = 'Coding For All'
print(company[0:7])

# Task 10: Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding')) # Returns the index of the first occurrence of 'Coding'

# Task 11: Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# Task 12: Change "Python for Everyone" to "Python for All" using the replace method or other methods.
sentence = 'Python for Everyone'
print(sentence.replace('Everyone', 'All'))

# Task 13: Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# Task 14: "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

# Task 15: What is the character at index 0 in the string Coding For All.
print(company[0])

# Task 16: What is the last index of the string Coding For All.
print(len(company) - 1)

# Task 17: What character is at index 10 in "Coding For All" string.
print(company[10])

# Task 18: Create an acronym or an abbreviation for the name 'Python For Everyone'.
name = 'Python For Everyone'
acronym = ''.join(word[0] for word in name.split())
print(acronym)

# Task 19: Create an acronym or an abbreviation for the name 'Coding For All'.
name = 'Coding For All'
acronym = ''.join(word[0] for word in name.split())
print(acronym)

# Task 20: Use index to determine the position of the first occurrence of C in Coding For All.
print(name.index('C'))

# Task 21: Use index to determine the position of the first occurrence of F in Coding For All.
print(name.index('F'))

# Task 22: Use rfind to determine the position of the last occurrence of l in Coding For All People.
string = 'Coding For All People'
print(string.rfind('l'))

# Task 23: Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

# Task 24: Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind('because'))

# Task 25: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])

# Task 26: Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# Task 27: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])

# Task 28: Does 'Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

# Task 29: Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

# Task 30: '   Coding For All      '  , remove the left and right trailing spaces in the given string.
sentence = '   Coding For All      '
print(sentence.strip())

# Task 31: Which one of the following variables return True when we use the method isidentifier():
s1 = '30DaysOfPython'
print(s1.isidentifier()) # False
s2 = 'thirty_days_of_python'
print(s2.isidentifier()) # True

# Task 32: The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

# Task 33: Use the new line escape sequence to separate the following sentences. I am enjoying this challenge. I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

# Task 34: Use a tab escape sequence to write the following lines.
print("Name\t\tAge\tCountry\tCity")
print("Rameen\t\t21\tPakistan\t\txyz")

# Task 35: Use the string formatting method to display the following:
radius = 10
pi = 3.14
area_of_circle = pi * (radius ** 2)
print(f"The area of a circle with radius {radius} is {area_of_circle:.2f}.")

# Task 36: Make the following using string formatting methods:
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))