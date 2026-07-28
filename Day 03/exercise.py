import math
# Task 1: Declare your age as integer variable
age = 21

# Task 2: Declare your height as a float variable
height = 4.11

# Task 3: Declare a variable that store a complex number
complex_number = 1 + 1j

# Task 4: Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input('Enter base of triangle: '))
height = float(input('Enter height of triangle: '))
area_of_triangle = (0.5 * base * height)
print('Area of Triangle:', area_of_triangle)

# Task 5: Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = float(input('Enter side a of triangle: '))
b = float(input('Enter side b of triangle: '))
c = float(input('Enter side c of triangle: '))
perimeter = a + b + c
print('Perimeter of triangle:', perimeter)

# Task 6: Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input('Enter length of rectangle: '))
width = float(input('Enter width of rectangle: '))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print('Area of rectangle:', area_of_rectangle)
print('Perimeter of rectangle:', perimeter_of_rectangle)

# Task 7: Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
radius = float(input('Enter radius of circle: '))
area_of_circle = pi * (radius ** 2)
circum_of_circle = 2 * pi * radius
print('Area of circle:', area_of_circle)
print('Circumference of circle:', circum_of_circle)

# Task 8: Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope1 = 2
# x-intercept is the value of x, when y = 0
x = 2 / 2
# y-intercept is the value of y, when x = 0
y = (2 * 0) - 2
print('Slope:', slope1)
print('x-intercept:', x)
print('y-intercept:', y)

# Task 9: Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1, x2, y2 = 2, 2, 6, 10
dx = x2 - x1
dy = y2 - y1
if dx != 0:
    slope2 = dy / dx
    print('slope:', slope2)
else:
    print('x is 0, so it not possible to find slope')

distance = (dx ** 2) + (dy ** 2)
euclidean_distance = math.sqrt(distance)
print('Euclidean distance:', euclidean_distance)

# Task 10: Compare the slopes in tasks 8 and 9.
if dx != 0:
    if slope1 == slope2:
       print("Slope 1 and Slope 2 are equal")
    elif slope1 > slope2:
       print("Slope 1 is greater than Slope 2")
    else:
       print("Slope 1 is smaller than Slope 2")
else:
    print('Slope 2 does not exist')

# Task 11: Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3
y = (x ** 2) + (6 * x) + 9
print('y =', y)
print('-3 is the value that makes y = x^2 + 6x + 9, 0')

# Task 12: Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') > len('dragon'))

# Task 13: Use and operator to check if 'on' is found in both 'python' and 'dragon'
print(('on' in 'python') and ('on' in 'dragon'))

# Task 14: I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon.')

# Task 15: There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

# Task 16: Find the length of the text python and convert the value to float and convert it to string
length_of_py = len('python')
float_py = float(length_of_py)
string_py = str(float_py)
print('Length of word Python:', length_of_py)
print('Converted to Float:', float_py)
print('Converted to String:', string_py)

# Task 17: Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input('Enter a number to check if its even or odd: '))
def is_even(number):
    return number % 2 == 0
print(is_even(number))

# Task 18: Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor = 7 // 3
integer = int(2.7)
def is_equal(floor, integer):
    return floor == integer
print(is_equal(floor, integer))

# Task 19: Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# Task 20: Check if float('9.8') is equal to 10
print(float('9.8') == 10) 

# Task 21: Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input('Enter your working hours: '))
rate = float(input('Enter rate per hour: '))
pay = hours * rate
print('Pay:', pay)

# Task 22: Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years: "))
seconds = years * 365 * 24 * 60 * 60
print("A person can live", seconds, "seconds.")

# Task 23: Write a Python script that displays the following table
# Display the table
for n in range(1, 6):
    print(n, 1, n, n ** 2, n ** 3)