# Assignment Operators

x = 1 # same as x = 1
x += 1 # x = x + 1
x -= 1 # x = x - 1
x *= 1 # x = x * 1
x /= 1 # x = x / 1
x %= 1 # x = x % 1
x //= 1 # x = x // 1
x **= 1 # x = x ** 1
x &= 1 # x = x & 1   AND operation
x |= 1 # x = x | 1   OR operation
x ^= 1 # x = x ^ 1   XOR operation
x >>= 1 # x = x >> 1  Right shift
x <<= 1 # x = x << 1  Left shift

print('Addition:', 1 + 2)
print('Subtraction:', 9 - 1)
print('Subtraction:', 1 - 9)
print('Multiplication:', 3 * 5)
print('Division:', 8 / 2)
print('Division:', 7 / 3)
print('Floor Division:', 7 // 2)
print('Remainder:', 6 % 3)
print('Remainder:', 7 % 3)
print('Exponentiation:', 2 ** 3)

print('Floating Number, PI:', 3.14)
print('Floating Number, Gravity:', 9.81)

print('Complex Number:', 1 + 1j)
print('Multiplying Complex Number:', (1 + 1j) * (1 - 1j))

length = 10
width = 5
area_of_rectangle = length * width
print('Area of Rectangle:', area_of_rectangle)

mass = 60
gravity = 9.81
weight = mass * gravity
print('Weight of an object:', weight)

mass = 60
volume = 0.06
density = mass / volume
print('Density of an object:', density)

# Comparison Operators

print(3 > 2) # Print True to the console
print(3 >= 2) # Print True to the console
print(3 < 2) # Print False to the console
print(2 < 3) # Print True to the console
print(7 <= 10) # Print True to the console
print(5 == 5) # Print True to the console
print(3 == 9) # Print False to the console
print(11 != 13) # Print True to the console
print(11 != 11) # Print False to the console

print(len('rameen') == len('tahir')) # Print False to the console
print(len('python') == len('dragon')) # Print True to the console
print(len('biryani') >= len('pizza')) # Print True to the console
print(len('cat') < len('tiger')) # Print True to the console
print(len('dog') < len('elephant')) # Print True to the console
print(len('bird') <= len('butterfly')) # Print True to the console
print(len('fish') == len('shark')) # Print False to the console
print(len('flower') == len('tree')) # Print False to the console
print(len('star') != len('moon')) # Print True to the console
print(len('sun') != len('sun')) # Print False to the console

print('True == True', True == True) # Print True to the console
print('True == False', True == False) # Print False to the console
print('False == False', False == False) # Print True to the console

print('1 is 1', 1 is 1) # Print True to the console
print('1 is not 2', 1 is not 2) # Print True to the console
print('r is in rameen', 'r' in 'rameen') # Print True to the console
print('h not in rameen', 'h' not in 'rameen') # Print True to the console

print('1 is 2', 1 is 2) # Print False to the console
print('1 is not 1', 1 is not 1) # Print False to the console
print('z is in rameen', 'z' in 'rameen') # Print False to the console
print('r not in rameen', 'r' not in 'rameen') # Print False to the console

# Logical Operators

print(9 > 2 and 4 > 3) # Print True to the console
print(5 > 3 and 1 > 2) # Print False to the console
print(9 < 10 and 5 > 6) # Print False to the console
print('True and True:', True and True) # Print True to the console
print('True and False:', True and False) # Print False to the console
print('False and False:', False and False) # Print False to the console

print(5 > 3 or 1 < 2) # Print True to the console
print(5 > 3 or 4 > 5) # Print True to the console
print(5 < 3 or 6 > 7) # Print False to the console
print('True or True:', True or True) # Print True to the console
print('True or False:', True or False) # Print True to the console
print('False or False:', False or False) # Print False to the console

print(not True) # Print False to the console
print(not False) # Print True to the console
print(not not True) # Print True to the console
print(not not False) # Print False to the console
