# if statement
a = 3
if a > 0:
    print('Positive')

# if-else
a = 3
if a > 0:
    print('Positive')
else:
    print('Negative')

# if elif else
a = 3
if a > 0:
    print('Positive')
elif a < 0:
    print('Negative')
else:
    print('Zero')

# Short end
a = 3
print('Positive') if a > 0 else print('Negative')

# Nested Conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is positive and even')
    else:
        print('A is positive and odd')
elif a < 0:
    if a % 2 == 0:
            print('A is negative and even')
    else:
            print('A is negative and odd')
else:
     print('Zero')

# If Condition and Logical Operators
a = 0
if a > 0 and a % 2 == 0:
    print('A is positive and even')
elif a > 0 and a % 2 != 0:
    print('A is positive and odd')
elif a < 0:
     print('Negative')
else:
     print('Zero')

# If and Or Logical Operators
user = 'James'
acces_level = 3
if user == 'James' or acces_level >= 4:
     print('Access granted')
else:
     print('Access denied')