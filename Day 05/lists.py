# Creating a List
# Using built in function list()
lst = list()
empty_list = list() # Empty list
print(len(empty_list))
# Using square brackets
lst = []
empty_list = [] # Empty list
print(len(empty_list))

# Creating a list with initial values
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['potato', 'tomato', 'cabbage', 'onion', 'carrot']
grocery = ['milk', 'meat', 'yoghurt', 'honey', 'butter']
web = ['HTML', 'CSS', 'React', 'Redux', 'Node']
countries = ['Finland', 'Denmark', 'Sweden', 'Norway', 'Iceland']

# Printing lists and its lengths
print('Fruits:', fruits)
print(len(fruits))
print('Vegetables:', vegetables)
print(len(vegetables))
print('Grocery:', grocery)
print(len(grocery))
print('Web:', web)
print(len(web))
print('Countries:', countries)
print(len(countries))
# Lists can have items of different data types
lst = ['Rameen', 21, True, {'country':'Pakistan', 'city':'xyz'}]
print(lst)

# Accessing lists using index
fruits = ['mango', 'orange', 'banana', 'lemon']
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_fruit = fruits[3]
print(last_fruit)
last_index = len(fruits) - 1
print('Last index:', last_index)
last_fruit = fruits[last_index]
print(last_fruit)

# Accessing List using Negative Indexing
fruits = ['mango', 'orange', 'banana', 'lemon']
first_fruit = fruits[-4]
print(first_fruit)
second_last = fruits[-2]
print(second_last)
last_fruit = fruits[-1]
print(last_fruit)

# Unpacking List Items
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

fruits = ['banana', 'orange', 'mango', 'apple', 'strawberry', 'peach']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first, second, third, *rest, tenth= lst
print(first)
print(second)
print(third)
print(rest)
print(tenth)

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# Slicing Items from the List
# Positive Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
print(all_fruits)
all_fruits = fruits[0:] # it also means all_fruits = fruits[0:4]
print(all_fruits)
orange_mango = fruits[1:3]
print(orange_mango)
orange_mango_lemon = fruits[1:4]
print(orange_mango_lemon)
orange_lemon = fruits[1:4:2]
print(orange_lemon)
# Negative Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]
print(all_fruits)
orange_mango = fruits[-3:-1]
print(orange_mango)
orange_mango_lemon = fruits[-3:]
print(orange_mango_lemon)
reverse_fruits = fruits[::-1]
print(reverse_fruits)

# Modifying List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
fruits[0] = 'avocado'
print(fruits)
fruits[1] = 'apple'
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = 'kiwi'
print(fruits)

# Checking Items in the List
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'lime' in fruits
print(does_exist)

# Adding Items to the List
lst = list()
lst.append('item1')
print(lst)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)

# Inserting Items into the List
lst = ['item1', 'item2']
lst.insert(1, 'item3')
print(lst)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')
print(fruits)
fruits.insert(3, 'lime')
print(fruits)

# Removing Items from the List
lst = ['item1', 'item2']
lst.remove('item1')
print(lst)
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)
fruits.remove('lemon')
print(fruits)

# Removing Items Using pop()
lst = ['item1', 'item2', 'item3']
lst.pop()
print(lst)
lst.pop(0)
print(lst)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)

# Removing Items Using Del
lst = ['item1', 'item2']
del lst[0]
print(lst)
del lst
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:3]
print(fruits)
del fruits

# Clearing List Items
lst = ['item1', 'item2']
lst.clear()
print(lst)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

# Copying a List
lst = ['item1', 'item2']
list_copy = lst.copy()
print(list_copy)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

# Joining Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)
positive_numbers = [1, 2, 3]
zero = [0]
negative_numbers = [-3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )

# Joining using extend() method
list1 = ['item1', 'item2']
list2 = ['item3', 'item4']
list1.extend(list2)
print(list1)
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print(num1)
negative_numbers = [-3, -2, -2]
zero = [0]
positive_numbers = [1, 2, 3]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and Vegetables:', fruits)

# Counting Items in a List
lst = ['item1', 'item2']
print(lst.count('item1'))
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Number of times Orange occured:', fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print('Number of times 24 occured:', ages.count(24))

# Finding Index of an Item in a List
lst = ['item1', 'item2']
print(lst.index('item1'))
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Index of Orange:', fruits.index('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print('First occurance of 24:', ages.index(24)) # Prints first index of 24

# Reversing a List
lst = ['item1', 'item2']
print(lst.reverse())
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Fruits:', fruits.reverse())
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.reverse())

# Sorting List Items
lst = ['item1', 'item2']
print(lst.sort())
print(lst.sort(reverse=True))
# sort()
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.sort())
print(fruits.sort(reverse=True))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.sort())
print(ages.sort(reverse=True))
# sorted()
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))
print(sorted(fruits, reverse=True))