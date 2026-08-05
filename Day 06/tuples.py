# Creating an Empty Tuple
empty_tuple = tuple()
empty_tuple = ()

tpl = ('item1', 'item2', 'item3', 'item4')
fruits = ('banana', 'orange', 'mango', 'lemon')

print('Length of tuple:', len(tpl))
print('Length of fruits:', len(fruits))

# Accessing Tuples

# Positive indexing
first_item = tpl[0]
second_item = tpl[1]
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print('First Fruit:', first_fruit)
print('Second Fruit:', second_fruit)
print('Last Fruit:', last_fruit)

# Negative Indexing
first_item = tpl[-4]
second_item = tpl[-3]
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
print('First Fruit:', first_fruit)
print('Second Fruit:', second_fruit)
print('Last Fruit:', last_fruit)

# Slicing Tuples
all_tuples = tpl[0:4]
print('All tuples:', all_tuples)
all_tuples = tpl[0:]
print('All tuples:', all_tuples)
middle_tuples = tpl[1:3]
print('Middle tuples:', middle_tuples)

all_fruits = fruits[0:4]
print('All Fruits:', all_fruits)
orange_mango = fruits[1:3]
print('orange and mango:', orange_mango)
orange_and_after = fruits[1:]
print('Orange and so on:', orange_and_after)

all_tuples = tpl[-4:]
print('All tuples:', all_tuples)
middle_tuples = tpl[-3:-1]
print('Middle tuples:', middle_tuples)

all_fruits = fruits[-4:]
print('All Fruits:', all_fruits)
orange_mango = fruits[-3:-1]
print('orange and mango:', orange_mango)
orange_and_after = fruits[-3:]
print('Orange and so on:', orange_and_after)

# Changing Tuple to List
lst = list(tpl)
print('List:', lst)

fruits = list(fruits)
print('Fruits List:', fruits)
fruits[0] = 'apple'
print('Fruits changed:', fruits)
fruits = tuple(fruits)
print('Tuple Fruits:', fruits)