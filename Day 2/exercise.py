# Exercise: Level 1

# Task 2: Write a python comment saying 'Day 2: 30 Days of python programming'
# Day2: 30 Days of Python Programming

# Task 3: Declare a first name variable and assign a value to it
first_name = 'Rameen'

# Task 4: Declare a last name variable and assign a value to it
last_name = 'Tahir'

# Task 5: Declare a full name variable and assign a value to it
full_name = first_name + ' ' + last_name

# Task 6: Declare a country variable and assign a value to it
country = 'Pakistan'

# Task 7: Declare a city variable and assign a value to it
city = 'xyz'

# Task 8: Declare an age variable and assign a value to it
age = 21

# Task 9: Declare a year variable and assign a value to it
year = 2004

# Task 10: Declare a variable is_married and assign a value to it
is_married = False

# Task 11: Declare a variable is_true and assign a value to it
is_true = True

# Task 12: Declare a variable is_light_on and assign a value to it
is_light_on = True

# Task 13: Declare multiple variable on one line
# first_name, last_name, age, city = 'Rameen', 'Tahir', 21, 'xyz' 

# Exercise: Level 2

# Task 1: Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Task 2: Using the len() built-in function, find the length of your first name
l_first = len(first_name)
l_last = len(last_name)

print("Length of first name:", l_first)
print("Length of last name:", l_last)

# Task 3: Compare the length of your first name and your last name
if l_first == l_last:
    print("First and last name are of equal length")
elif l_first > l_last:
    print("First name is longer than last name")
else:
    print("Last name is longer than first name")

# Task 4: Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Task 5: Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print("Sum:", total)

# Task 6: Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print("Difference:", diff)

# Task 7: Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print("Product:", product)

# Task 8: Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print("Quotient:", division)

# Task 9: Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print("Remainder:", remainder)

# Task 10: Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print("Power:", exp)

# Task 11: Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print("Floor division:", floor_division)

# Task 12: The radius of a circle is 30 meters.
r = 30
pi = 3.14
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = pi * (r ** 2)
print("Area of Circle:", area_of_circle)
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * pi * r
print("Circumference of Circle:", circum_of_circle)
# Take radius as user input and calculate the area.
radius = float(input("Enter the radius of the circle: "))
area_of_circle = pi * (radius ** 2)
print("Area of Circle:", area_of_circle)

# Task 13: Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
countr = input("Enter your country: ")
agee = input("Enter your age: ")
print("First Name:", f_name)
print("Last Name:", l_name)
print("Country:", countr)
print("Age:", agee)

# Task 14: Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
#help('keywords')