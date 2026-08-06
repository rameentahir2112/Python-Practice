# Exercise
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Level 1

# Task 1: Find the length of the set it_companies
print('Length of IT companies set:', len(it_companies))

# Task 2: Add 'Twitter' to it_companies
it_companies.add('Twitter')

# Task 3: Insert multiple IT companies at once to the set it_companies
it_companies.update(['Cisco', 'Meta'])

# Task 4: Remove one of the companies from the set it_companies
it_companies.remove('Meta')

# Task 5: What is the difference between remove and discard
# set.remove(x): removes an item and causes an error
# set.discard(x): removes an item and does not cause an error

# Level 2

# Task 1: Join A and B
ab = A.union(B)
print('Union of A and B:', ab)

# Task 2: Find A intersection B
ab = A.intersection(B)
print('Intersection of A and B:', ab)

# Task 3: Is A subset of B
print('Is A subset of B?', A.issubset(B))

# Task 4: Are A and B disjoint sets
print('Are A and B disjoint sets?', A.isdisjoint(B))

# Task 6: What is the symmetric difference between A and B
print('symmetric difference between A and B:', A.symmetric_difference(B))

# Task 5: Join A with B and B with A
A.update(B)
B.update(A)

# Task 7: Delete the sets completely
del it_companies
del A
del B
del ab

# Level 3:

# Task 1: Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_age = set(age)
len_set = len(set_age)
len_list = len(age)
if len_set < len_list:
    print('List is longer')
else:
    print('Set and list are equal')

# Task 2: Explain the difference between the following data types: string, list, tuple and set
# A string holds text, a list is a changeful group of items, a tuple is a fixed group of items, and a set holds unique items in no order.

# Task 3: I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
words = sentence.split()
unique_words = set(words)
print('Number of unique words:', len(unique_words))