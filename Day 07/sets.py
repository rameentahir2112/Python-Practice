# Creating an Empty Set
st = set()

# Creating a set with initial items
st = {'item1', 'item2', 'item3', 'item4'}
fruits = {'banana', 'orange', 'mango', 'lemon'}

# Length of Sets
print('Length of Set:', len(st))
print('Length of Fruits:', len(fruits))

# Checking if an item exist in the set
print('Does item3 exist in set?', 'item3' in st)
print('Does mango exist in set of fruits?', 'mango' in fruits)

# Adding an item to the set
# Add one item using add()
st.add('item5')
fruits.add('lime')
# Add multiple items using update()
st.update(['item6', 'item7', 'item8'])
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

# Removing Items from a set
# Using remove()
st.remove('item2')
print('Set after removing item2:', st)
# Using pop()
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print('The removed fruit is:', removed_item)

# Clearing a set
st.clear()
print(st)
fruits.clear()
print(fruits)

# Deleting a set
st = {'item1', 'item2', 'item3', 'item4'}
del st
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

# Converting list to set
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)
print('List converted to set:', st)
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits)
print('Fruits list converted to set:', fruits)

# Joining sets
# Using union()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print('Set 1 and set 2 joined:', st3)
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits_and_vegies = fruits.union(vegetables)
print('Fruits and Vegetables combined;', fruits_and_vegies)
# Using update() # This method inserts a set into a given set
st1 = {'item1', 'item2', 'item3'}
st2 = {'item4', 'item5', 'item6'}
st1.update(st2) # st2 contents are added to st1
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print('Fruits and Vegetables:', fruits)

# Finding Intersection Items
st1 = {'item1', 'item2', 'item3'}
st2 = {'item2', 'item3'}
print('Intersection of two set:', st1.intersection(st2))
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0 ,2 ,4 ,6 ,8, 10}
print('Even numbers:', whole_numbers.intersection(even_numbers))
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print('Common letters in Python and Dragon:', python.intersection(dragon))

# Checking Subset and Super Set
# issubset(): small_set.issubset(big_set)
# issuperset(): big_set.issuperset(small_set)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print('Is set 2 a subset of set 1?', st2.issubset(st1))
print('Is set 1 a super set of set 2?', st1.issuperset(st2))
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0 ,2 ,4 ,6 ,8, 10}
print('Are whole numbers a subset of even numbers?', whole_numbers.issubset(even_numbers))
print('Are whole numbers a super set of even numbers?', whole_numbers.issuperset(even_numbers))
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print('Is python a subset of dragon?', python.issubset(dragon))

# Checking the Difference Between Two Sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print('set2 - set1:', st2.difference(st1))
print('set1 - set2:', st1.difference(st2))
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print('Whole numbers - even numbers:', whole_numbers.difference(even_numbers))
python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print('python - dragon:', python.difference(dragon))
print('dragon - python:', dragon.difference(python))

# Finding Symmetric Difference Between Two Sets
# (A-B)U(B-A) contains all uncommon items
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print('Symmetric Difference:', st2.symmetric_difference(st1))
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print('Symmetric difference of whole numbers with some provided numbers:', whole_numbers.symmetric_difference(some_numbers))
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print('Symmetric difference of python and dragon:', python.symmetric_difference(dragon))

# Disjoint sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print('Are set1 and set2 disjoint sets?', st1.isdisjoint(st2))
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print('Are whole numbers and even numbers disjoint sets?', even_numbers.isdisjoint(odd_numbers))
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print('Are python and dragon disjoint?', python.isdisjoint(dragon))