# Exercise

# Level 1

# Task 1: Create an empty tuple
empty_tuple = ()

# Task 2: Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Fatima', 'Zainab', 'Maryam')
brothers = ('Ali', 'Abdullah', 'Ahmed')

# Task 3: Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# Task 4: How many siblings do you have?
print('Number of Siblings:', len(siblings))

# Task 5: Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.append('Hassan') 
family_members.append('Ayesha') 

# Level 2

# Task 1: Unpack siblings and parents from family_members
*siblings, father, mother = family_members
print('Father:', father)
print('Mother:', mother)
print('Siblings:', siblings)

# Task 2: Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Banana', 'Orange', 'Mango')
vegetables = ('Tomato', 'Potato', 'Carrot')
animal_products = ('Meat', 'Milk', 'Eggs')
food_stuff_tp = fruits + vegetables + animal_products
print('Food:', food_stuff_tp)

# Task 3: Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Task 4: Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    print('Middle Food Items:', food_stuff_lt[middle_index - 1], 'and', food_stuff_lt[middle_index])
else:
    print('Middle Food Item:', food_stuff_lt[middle_index])

# Task 5: Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[0:3]
print('First three food items:', first_three)
last_three = food_stuff_lt[-3:]
print('Last three food items:', last_three)

# Task 6: Delete the food_stuff_tp tuple completely
food_stuff_tp = tuple(food_stuff_lt)
del food_stuff_tp

# Task 7: Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
is_nordic = 'Estonia' in nordic_countries
print('Is Estonia a nordic country?', is_nordic)
is_nordic = 'Iceland' in nordic_countries
print('Is Iceland a nordic country?', is_nordic)